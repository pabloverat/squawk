class Squawk:
  
  def __init__(self, squawk_data):
    self.squawk_id = squawk_data[0]
    self.content = squawk_data[1]
    self.is_reply_to = squawk_data[2]
    self.user_id = squawk_data[3]
    self.created = squawk_data[4]
  
  def get_squawk_id(self):
    return self.squawk_id

  def get_content(self):
    return self.content

  def get_is_reply_to(self):
    return self.is_reply_to

  def get_user_id(self):
    return self.user_id

  def get_created(self):
    return self.created
  
  def set_squawk_id(self, squawk_id):
    self.squawk_id = squawk_id

  def set_content(self, content):
    self.content = content

  def set_is_reply_to(self, is_reply_to):
    self.is_reply_to = is_reply_to

  def set_user_id(self, user_id):
    self.user_id = user_id

  def set_created(self, created):
    self.created = created

  def to_dict(self):
    return {
      'squawk_id': self.squawk_id,
      'content': self.content,
      'is_reply_to': self.is_reply_to,
      'user_id': self.user_id
    }