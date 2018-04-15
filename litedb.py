import sqlite3

class Database():

	
	def __init__(self):
		self.con = sqlite3.connect('users.db')
		self.cur = self.con.cursor()
	def execread(self,query):
		self.cur.execute(query)
		result = self.cur.fetchall()
		return result
	def execwrite(self,query):
		self.cur.execute(query)
		self.con.commit()

	def close(self):
		self.con.close()


