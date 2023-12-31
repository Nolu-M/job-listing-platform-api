import os 

from psycopg2 import pool

conn_pool = pool.SimpleConnectionPool(
  1, 100,
  database=os.getenv('DB_NAME'),
  host=os.getenv('DB_HOST'),
  port=os.getenv('DB_PORT'),
  user=os.getenv('DB_USER'),
  password=os.getenv('DB_PASS')
)


class db:
  def __init__(self, table):
    self.table = table
    self.pool = conn_pool

  def select(self, condition=None):
    conn = self.pool.getconn()
    cursor = conn.cursor()

    cursor.execute(f'SELECT * FROM {self.table} {condition} ORDER BY id ASC')

    return cursor.fetchall()

  def insert(self, columns, values):
    conn = self.pool.getconn()
    cursor = conn.cursor()

    sql = f"INSERT INTO {self.table} ({columns}) VALUES ({values}) RETURNING id;"
    
    cursor.execute(sql)

    curr_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return curr_id
  

  

