import sqlite3

from bl.event import Event
from utils.database import Database


class EventDAO:
  def __init__(self):
    self.DB = Database()
  
  def create(self, event):
    query = "INSERT INTO event (type_of_action, user_id) VALUES (?, ?)"
    values = (event.type_of_action, event.user_id)
    self.DB.execute(query, values)
    self.DB.commit()
    
  def delete(self, eventID):
    query = "DELETE FROM event WHERE event_id = ?"
    self.DB.execute(query, (eventID, ))
    self.DB.commit()

  def get(self, eventID):
    query = "SELECT * FROM event WHERE event_id = ?"
    result = self.DB.execute(query, (eventID, ))
    try:
      data = result.fetchone()
      if data:
        event = Event(data)
        return event
      return None
    except:
      return None

  def update(self, event):
    query = "UPDATE event SET type_of_action = ?, user_id = ? WHERE event_id = ?"
    values = (event.type_of_action, event.user_id, event.event_id)
    self.DB.execute(query, values)
    self.DB.commit()