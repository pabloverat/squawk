from bl.user import User
from dl.user_dao import UserDAO


class UserService:
  def __init__(self):
    self.userDAO = UserDAO()

  def delete_user(self, user_id):
    self.userDAO.delete(user_id)

  def get_user(self, user_id):
    user = self.userDAO.get(user_id)
    return user

  def get_user_by_name(self, username):
    user = self.userDAO.get_by_name(username)
    return user

  def signup(self, username, password):
    debug = self.userDAO.get_by_name(username)
    print(debug)
    if debug is not None:
      return False
    else:
      user = User((None, username, password, None))
      self.userDAO.create(user)
      return True

  def login(self, username, password):
    user = self.userDAO.get_by_name(username)
    if user is None:
      return "user_unknown"

    if user.password != password:
      return "password_mismatch"

    return "success"

  def update_user(self, user_id, username, password, is_admin):
    user = self.userDAO.get(user_id)
    if user:
      user.username = username
      user.password = password
      user.is_admin = is_admin
      self.userDAO.update(user)