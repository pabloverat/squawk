class Event:
  def __init__(self, type_of_action, user_id):
    self.event_id = None
    self.type_of_action = type_of_action
    self.user_id = user_id
    self.created = None

  def get_event_id(self):
    return self.event_id

  def get_type_of_action(self):
    return self.type_of_action

  def get_user_id(self):
    return self.user_id

  def get_timestamp(self):
    return self.created