import asyncio
import random
import string
import uuid as uuidlib
from datetime import datetime

import sqlalchemy as sa
from aiohttp import web
from aiopg.sa import create_engine
from faker import Faker
from faker.providers import date_time, internet, lorem
from simcore_postgres_database.models.base import metadata
from simcore_postgres_database.settings import build_url
from simcore_postgres_database.webserver_models import *
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.schema import CreateTable, DropTable

fake = Faker()
fake.add_provider(internet)
fake.add_provider(date_time)
fake.add_provider(lorem)


def init_tables(cfg):
  print("init_tables")
  url = build_url(**cfg)
  e = sa.create_engine(str(url), echo=True)
  try:
    metadata.create_all(e, checkfirst=True)
  finally:
    e.dispose()

async def insert_data(conn):
  # TODO: add fakes
  async with conn.begin(): # transction
    # I think this roolbacks if fails
    user_email = fake.email()
    uid = await conn.scalar(users.insert().values(
        name=user_email.split("@")[0],
        email=user_email,
        password_hash="".join(random.choices(
            string.ascii_letters+string.digits, k=10)),
        status=UserStatus.ACTIVE,
        role=random.choice(list(UserRole))
    ))

  # Add projects for user
  for _ in range(random.randint(0,10)):
    async with conn.begin():
      # create
      pid = await conn.scalar(projects.insert().values(
        type=random.choice(list(ProjectType)),
        uuid= uuidlib.uuid1(),
        name= " ".join(fake.words(nb=3, ext_word_list=None, unique=True)),
        description=fake.paragraph(
            nb_sentences=3, variable_nb_sentences=True, ext_word_list=None),
        thumbnail=fake.image_url(),
        prj_owner=user_email,
        creation_date=datetime.utcnow(),
        last_change_date=datetime.utcnow(),
        workbench={}, # create json from schema
        published= random.random()<0.5
      ))
      # assign
      await conn.execute( user_to_projects.insert().values(
        user_id = uid,
        project_id = pid
      ))

async def prepare_tables(pg):
  print("prepare_tables")
  async with pg.acquire() as conn:
    for table in [users, user_to_projects, projects]:
      try:
        query = CreateTable(table)
        print(query)
        await conn.execute(query)
      except psycopg2.ProgrammingError:
        pass

async def init_pg(app):
  print("init_pg")
  db_conf = app['config']['database']

  cfg = dict(
    database = db_conf['name'],
    user = db_conf['user'],
    password = db_conf['password'],
    host = db_conf['host'],
    port = db_conf['port']
  )
  engine = await create_engine(echo=True, **cfg)
  init_tables(cfg)
  #await prepare_tables(engine)
  app['db'] = engine

async def close_pg(app):
  print("close_pg")
  app['db'].close()
  await app['db'].wait_closed()
  del app['db']

async def pg_cleanup_ctx(app):
  await init_pg(app)
  yield
  await close_pg(app)

async def deep_delete_user(uid, conn):
  with conn.begin():
    query = user_to_projects.delete().where(user_to_projects.c.user_id == uid)
    
    projects.delete().

    query = users.delete().where(users.c.id == uid)

    result = await conn.execute(users_to_projects.select(
      [user_to_projects.c.project_id]).where(
      user_to_projects.c.user_id == uid))
    
    async for pid in result.fetchall()
      await conn.execute(project.delete().where(project.c.id=pid))







# Handlers ---------------
async def hi(request):
  raise web.Response(text="hoi")

async def insert(app):
  async with app['db'].acquire() as conn:
    await asyncio.sleep(10)
    await insert_data(conn)

async def populate(request):
  N = request.query.get('num_users', 1)
  errors = await asyncio.gather(*[insert(request.app) 
      for _ in range(N)], return_exceptions=True)

  if any(errors):
    msg = " ".joint([e.reason for e in errors if e])
    raise web.HTTPServerError(text=msg)
  raise web.HTTPOk()

async def delete_user(request: web.Request):
  uid = request.match_info["id"]
  async with app['db'].acquire() as conn:
    await deep_delete_user(uid, conn)

def main():
  app = web.Application()
  app['config'] = {
    'database': {
      'name': 'db',
      'user': 'test',
      'password': 'test',
      'host': '127.0.0.1',
      'port': 5432
    }
  }
  app.add_routes([
    web.get("/", hi),
    web.post("/insert", populate),
    web.delete("/users/{id}", delete_user)
  ])
  app.cleanup_ctx.append(pg_cleanup_ctx)
  web.run_app(app, host='127.0.0.1', port=8080)


if __name__ == "__main__":
  main()
