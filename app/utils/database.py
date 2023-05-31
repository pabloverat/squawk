import sqlite3


class Database:
  def __init__(self):
    self.DB = "app/utils/db.sqlite"
    self.connection = None
    self.connect()

  def connect(self):
    try:
      self.connection = sqlite3.connect(self.DB, check_same_thread=False)
      print("Connected to the DB.")
    except sqlite3.Error:
      print(f"Error connecting to the DB: {sqlite3.Error}")

  def disconnect(self):
    if self.connection:
      self.connection.close()
      print("DB disconnected.")

  def run_query(self, query, parameters=None):
    try:
      cursor = self.connection.cursor()
      if parameters:
        cursor.execute(query, parameters)
      else:
        cursor.execute(query)
      self.connection.commit()
      return cursor
    except Exception as e:
      print(f"Error running query: {e}")
      return None