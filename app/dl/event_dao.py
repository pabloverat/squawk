from bl.event import Event
from utils.database import Database


class EventDAO:
  def __init__(self):
    self.DB = Database()
  
  def create(self, event):
    query = "INSERT INTO event (type_of_action, user_id) VALUES (?, ?)"
    values = (event.type_of_action, event.user_id)
    _ = self.DB.run_query(query, values)
    
  def delete(self, eventID):
    query = "DELETE FROM event WHERE event_id = ?"
    _ = self.DB.run_query(query, (eventID, ))

  def get_todays_logins(self):
    query = "SELECT COUNT(DISTINCT user_id) FROM event WHERE type_of_action = 1 AND DATE(created) = DATE('now');"
    result = self.DB.run_query(query)
    try:
      data = result.fetchone()
      return data # <- int
    except:
      return None

  def get_most_actions(self):
    query = "SELECT user_id, COUNT(*) as count FROM event WHERE DATE(created) = DATE('now') GROUP BY user_id ORDER BY count DESC"
    result = self.DB.run_query(query)
    try:
      data = result.fetchone()
      if data:
        return data
      return None
    except:
      return None
    
  def get_most_replied_today(self):
    query = "SELECT is_reply_to, COUNT(*) as count FROM squawks WHERE DATE(created) = DATE('now') AND is_reply_to != 0 GROUP BY is_reply_to ORDER BY count DESC;"
    result = self.DB.run_query(query)
    try:
      data = result.fetchone()
      return data
    except:
      return None

  def update(self, event):
    query = "UPDATE event SET type_of_action = ?, user_id = ? WHERE event_id = ?"
    values = (event.type_of_action, event.user_id, event.event_id)
    _ = self.DB.run_query(query, values)  