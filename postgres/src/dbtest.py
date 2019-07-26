import asyncio

import sqlalchemy as sa
from aiopg.sa import create_engine
from aiohttp import web


metadata = sa.MetaData()

tbl = sa.Table('tbl', metadata,
  sa.Column('id', sa.Integer, primary_key=True),
  sa.Column('val', sa.String(255))
)

async def pg_context(app: web.Application):
  cfg = app["config"]["db"]
  async with create_engine(**cfg) as engine:
    app['engine'] = engine

    yield engine

  




async def close_pg(app: web.Application):
  engine = app[""]


from sqlalchemy.schema import CreateTable

async def create_table(conn):
  print(asyncio.Task.current_task(loop), 'create_table')
  # Would be good to get this from tbl...!?
  await conn.execute("DROP TABLE IF EXISTS tbl")

  query = CreateTable(tbl)
  print(query)
  await conn.execute(query)
  #await conn.execute('''CREATE TABLE tbl (
  #                                      id serial PRIMARY KEY,
  #                                      val varchar(255)
  #                                      )
  #                    ''')

async def insert_data(conn, data):
  print(asyncio.Task.current_task(loop), 'inserting')
  await conn.execute(tbl.insert().values(val='abc'))

async def go():
  loop = asyncio.get_event_loop()
  async with create_engine( database="db",
                            user='test', password='test',
                            host='127.0.0.1', port=5432 ) as engine:
    async with engine.acquire() as conn:
      await create_table(conn)

      await insert_data(conn)
      
      async for row in conn.execute(tbl.select().where(tbl.c.val~='abc')):
        print(row)
        print(row.id, row.val)
        print(row[tbl.c.id], row[tbl.c.val])
        print(asyncio.Task.current_task(loop), 'retrieved')

      num_rows = await conn.scalar(tlb.count())
      print(num_rows)

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(go())