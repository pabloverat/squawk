
from bl.event import Event


class EventBuilder:
  def __init__(self):
    self.type_of_action = None
    self.user_id = None

  def with_type_of_action(self, type_of_action):
    self.type_of_action = type_of_action
    return self
  
  def with_user_id(self, user_id):
    self.user_id = user_id
    return self
  
  def build(self):
    return Event(type_of_action=self.type_of_action, user_id=self.user_id)