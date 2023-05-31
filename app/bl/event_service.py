from app.bl.event import Event
from app.dl.event_dao import EventDAO

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