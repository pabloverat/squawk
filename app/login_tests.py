import unittest

from bl.event_service import EventService
from bl.user_service import UserService
from flask import session

from app import app


class MainControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user_service = UserService()
        self.event_service = EventService()

    def test_login_success(self):
        # Create a test user
        username = "testuser"
        password = "password123"
        self.user_service.signup(username, password)

        # Make a POST request to login with the test user credentials
        response = self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

        # Check if the user is redirected to the home page
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, '/home')

        # # Check if the user ID is stored in the session
        # self.assertIn('user_id', session)
        # user_id = session['user_id']

        # Check if a login event is created
        events = self.event_service.get_events()
        last_event = events[-1]
        self.assertEqual(last_event[1], 1) # last_event[1] gets its type_of_action
        # self.assertEqual(last_event.user_id, user_id)

    def test_login_failure(self):
        # Make a POST request to login with invalid credentials
        response = self.app.post('/login', data=dict(
            username="invaliduser",
            password="wrongpassword"
        ), follow_redirects=True)

        # Check if the user is redirected back to the login page
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request.path, '/login')

        # Check if an error message is displayed
        self.assertIn(b'Incorrect username or password.', response.data)

if __name__ == "__main__":
    unittest.main()