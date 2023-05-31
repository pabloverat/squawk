from dl.squawk_dao import SquawkDAO


class ThreadService:
  def __init__(self):
    self.squawkDAO = SquawkDAO()

  def get_thread(self, squawk_id):
    squawk = self.squawkDAO.get(squawk_id)
    if not squawk:
      return []
      
    thread = self._get_replies(squawk_id)
    return thread

  def _get_replies(self, squawk_id):
    replies = []
    squawks = self.squawkDAO.getall()
    for x in squawks:
      if x.is_reply_to == squawk_id:
        replies.append(x)
    return replies