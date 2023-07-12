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