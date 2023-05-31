from bl.squawk import Squawk
from utils.database import Database


class SquawkDAO:
  def __init__(self):
    self.DB = Database()

  def create(self, squawk: Squawk):
    query = "INSERT INTO squawks (content, is_reply_to, user_id) VALUES (?, ?, ?)"
    values = (squawk.content, squawk.is_reply_to, squawk.user_id)
    _ = self.DB.run_query(query, values)
    # self.DB.commit()
  
  def delete(self, squawkID):
    query = "DELETE FROM squawks WHERE squawk_id = ?"
    _ = self.DB.run_query(query, (squawkID, ))
    # self.DB.commit()
  
  def get(self, squawkID):
    query = "SELECT * FROM squawks WHERE squawk_id = ?"
    result = self.DB.run_query(query, (squawkID, ))
    try:
    # if data:
      data = result.fetchone()
      squawk = Squawk(data)
      return squawk
    except:
      return None

  def getall(self):
    query = "SELECT * FROM squawks ORDER BY created DESC"
    result = self.DB.run_query(query)
    try:
      data_list = result.fetchall()
      squawks = []
      for data in data_list:
        squawk = Squawk(data)#['squawk_id'], data['content'], data['is_reply_to'], data['user_id'], data['created'])
        squawks.append(squawk)
      return squawks
    except:
      return None

  def getall_from(self, user_id):
    query = "SELECT * FROM squawks WHERE user_id = ? ORDER BY created DESC"
    result = self.DB.run_query(query, (user_id, ))
    try:
      data_list = result.fetchall()
      squawks = []
      for data in data_list:
        squawk = Squawk(data)#['squawk_id'], data['content'], data['is_reply_to'], data['user_id'], data['created'])
        squawks.append(squawk)
      return squawks
    except:
      return None

  def getall_super(self):
    query = "SELECT * FROM squawks WHERE is_reply_to = 0 ORDER BY created DESC"
    result = self.DB.run_query(query)
    try:
      data_list = result.fetchall()
      squawks = []
      for data in data_list:
        squawk = Squawk(data)
        squawks.append(squawk)
      return squawks
    except:
      return None

  def update(self, squawk):
    query = "UPDATE squawks SET content = ? WHERE squawk_id = ?"
    values = (squawk.content, squawk.squawk_id)
    self.DB.run_query(query, values)
    self.DB.commit()