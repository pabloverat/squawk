import unittest

from bl.event_service import EventService
from bl.user import User
from dl.event_dao import EventDAO
from dl.user_dao import UserDAO


class CommentTests(unittest.TestCase):
    def setUp(self):
        self.eventDAO = EventDAO()
        self.userDAO = UserDAO()
        self.event_service = EventService()

    def test_create_comment_event(self):
        # Create a test user
        test_user = User((None, "testuser", "password123", False))
        self.userDAO.create(test_user)
        test_user = self.userDAO.get_by_name(test_user.username)

        # Create a comment event
        self.event_service.create_event(2, test_user.user_id)

        # Get the created event from the DAO
        events = self.eventDAO.get_all()
        created_event = events[-1]

        # Assert that the event type and user ID are correct
        self.assertEqual(created_event[1], 2)
        self.assertEqual(created_event[2], str(test_user.user_id))


if __name__ == "__main__":
    unittest.main()