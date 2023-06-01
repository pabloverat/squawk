import sqlite3


class Database:
  __instance = None

  def __new__(self):
    if self.__instance is None:
      self.__instance = super().__new__(self)
    return self.__instance

  def __init__(self):
    if getattr(self, 'connection', None) is None:
      self.DB = "app/utils/db.sqlite"
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