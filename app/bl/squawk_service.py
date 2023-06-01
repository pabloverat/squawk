from bl.squawk import Squawk
from dl.squawk_dao import SquawkDAO


class SquawkService:
  def __init__(self):
    self.squawkDAO = SquawkDAO()

  def create_squawk(self, content, is_reply_to, user_id):
    if len(content) > 300:
      raise ValueError("Error! El contenido del squawk excede el máximo de 300 caracteres.")
    squawk = Squawk((None, content, is_reply_to, user_id, None))
    self.squawkDAO.create(squawk)

  def delete_squawk(self, squawk_id):
    self.squawkDAO.delete(squawk_id)

  def get_squawk(self, squawk_id):
    squawk = self.squawkDAO.get(squawk_id)
    return squawk

  def get_last(self, total, user_id):
    if user_id != -1:
      squawks = self.squawkDAO.getall_from(user_id)
    else:
      squawks = self.squawkDAO.getall_super()
    return squawks[:total]

  def update_squawk(self, squawk_id, content):
    if len(content) > 300:
      raise ValueError("Error! El contenido del squawk excede el máximo de 300 caracteres.")
    squawk = self.squawkDAO.get(squawk_id)
    if squawk:
      squawk.content = content
      self.squawkDAO.update(squawk)