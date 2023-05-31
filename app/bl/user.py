class User:  
  def __init__(self, data):
    self.user_id = data[0]
    self.username = data[1]
    self.password = data[2]
    self.is_admin = data[3]
    self.is_authenticated = False
    self.is_active = False
    self.is_anonymous = False
  

  def get_id(self):
    return self.user_id
  
  def get_username(self):
    return self.username
  
  def get_password(self):
    return self.password
  
  def is_admin(self):
    return self.is_admin

  def make_admin(self):
    self.is_admin = True

  def remove_admin(self):
    self.is_admin = False
  
  def set_id(self,user_id):
    self.user_id = user_id
  
  def set_username(self, username):
    self.username = username
  
  def set_password(self,password):
    self.password = password