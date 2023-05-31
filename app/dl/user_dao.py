from bl.user import User
from utils.database import Database


class UserDAO:
  def __init__(self):
    self.DB = Database()

  def create(self, user: User):
    query="INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)"
    values = (user.username, user.password, 0)
    _ = self.DB.run_query(query,values)
    # cursor.commit()

  def delete(self, user_id):
    query = "DELETE FROM users WHERE user_id = ?"
    _ = self.DB.run_query(query, (user_id, ))
    # self.DB.commit()

  def get(self, userID):
    query = "SELECT * FROM users WHERE user_id = ?"
    result = self.DB.run_query(query, (userID, ))
    try:
      data = result.fetchone()
      user = User(data)
      return user
    except:
      return None

  def get_by_name(self, username):
    query = "SELECT * FROM users WHERE username = ?"
    result = self.DB.run_query(query, (username, ))
    try:
      data = result.fetchone()
      user = User(data)
      return user
    except:
      return None
      


  def update(self, user):
    query = "UPDATE users SET username = ?, password = ?, is_admin = ? WHERE user_id = ?"
    values = (user.username, user.password, user.is_admin, user.user_id)
    _ = self.DB.run_query(query, values)
    # self.DB.commit()