import sqlalchemy as sa
from aiohttp import web
from aiopg.sa import create_engine
from simcore_postgres_database.settings import build_url
from simcore_postgres_database.webserver_models import *
from simcore_postgres_database.models.base import metadata
from sqlalchemy import create_engine as sa_create_engine
from sqlalchemy.schema import CreateTable, DropTable

def init_tables(cfg):
  print("init_tables")
  url = build_url(**cfg)
  e = sa.create_engine(str(url), echo=True)
  metadata.create_all(e, check_first=True)
  e.close()

import random
import uuid as uuidlib

def insert_data(conn):
  # TODO: add fakes
  async with conn.begin(): # transction
    # I think this roolbacks if fails
    user_email = "a@foo.com"
    uid = await conn.scalar(users.insert().values(
        name="abcd", 
        email=user_email,
        password_hash= "random", 
        status=UserStatus.ACTIVE,
        role=random.choice(list(UserStatus))
    ))

  # Add projects for user
  async with conn.begin():
    # create
    pid = await conn.scalar(projects.insert().values(
      type=random.choice(list(ProjectType))
      uuid=uuidlib.uuid1()
      name="project 1",
      description="adsf",
      thumbnail="http:/",
      prj_owner=user_email,
      creation_data=datetime.utcnow(),
      last_change_data=datetime.utcnow(),
      workbench={}, # create json from schema
      published=False
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


async def hi(request):
  raise web.Response(text="hoi")


async def populate(request):
  with app['db'].acquire() as conn:
    await insert_data(conn)
  raise web.HTTPOk()

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
    web.post("/populate", populate)
  ])
  app.cleanup_ctx.append(pg_cleanup_ctx)
  web.run_app(app, host='127.0.0.1', port=8080)


if __name__ == "__main__":
  main()
