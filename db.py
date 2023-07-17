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
<<<<<<< HEAD
 def __init__(self, table):
  self.table = table
  self.pool = conn_pool

  def insert(self,title,company,location,salary,description,requirements):
   conn = self.pool.getconn()
   cursor = conn.cursor()

   cursor.execute('INSERT INTO job_listings (title,company,location,salary,description,requirements) VALUES(%,%,%,%,%,%)')
   conn.commit()

   
   conn.close()

   return 201
  
  def select(self):
   conn = self.pool.getconn()
   cursor = conn.cursor()

   cursor.execute('SELECT * FROM job_listings ORDER BY id DESC')
=======
    def __init__(self, table):
        self.table = table
        self.pool = conn_pool

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
>>>>>>> 9eaac29bb22090c19a17101b213fb187e966012d
