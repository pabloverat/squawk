from abc import ABC, abstractmethod

from bl.user_service import UserService


class UserAuthStrategy(ABC):
  @abstractmethod
  def authenticate(self, username: str, password: str) -> bool:
    pass
  
class DBAuthStrategy(UserAuthStrategy):
  def __init__(self):
    self.user_service = UserService()

  def authenticate(self, username: str, password: str) -> bool:
    login = self.user_service.login(username, password)
    if login == "success": return True
    return False