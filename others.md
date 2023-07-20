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