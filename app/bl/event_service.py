from bl.event import Event
from dl.event_dao import EventDAO


class EventService:
  def __init__(self):
    self.eventDAO = EventDAO()

  def create_event(self, type_of_action, userID):
    event = Event(type_of_action=type_of_action, user_id=userID)
    self.eventDAO.create(event)

  def delete_event(self, eventID):
    self.eventDAO.delete(eventID)

  def get_event(self, eventID):
    pass

  def update_event(self, eventID, content):
    pass
  
  def get_report(self):
    popular_squawk = self.eventDAO.get_most_replied_today()
    active_user = self.eventDAO.get_most_actions()
    todays_logins = self.eventDAO.get_todays_logins()
    return popular_squawk, active_user, todays_logins