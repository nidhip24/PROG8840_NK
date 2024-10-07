import unittest
from unittest.mock import patch

from user import User, get_user, create_user

class TestUserApi(unittest.TestCase):

    @patch('user.users_db', new_callable=lambda: {1: User(1, "Alice", 30)})
    def test_get_user(self, mock_users_db):
        user_data, status_code = get_user(1)
        self.assertEqual(status_code, 200)
        self.assertEqual(user_data, {"user_id": 1, "name": "Alice", "age": 30})

    def test_get_non_existent_user(self):
        user_data, status_code = get_user(3)
        self.assertEqual(status_code, 404)
        self.assertEqual(user_data, {"error": "User not found"})

    @patch('user.users_db', new_callable=lambda: {1: User(1, "Alice", 30)})
    def test_create_user(self, mock_users_db):
        user_data, status_code = create_user("Charlie", 28)
        self.assertEqual(status_code, 201)
        self.assertEqual(user_data, {"user_id": 2, "name": "Charlie", "age": 28})

if __name__ == '__main__':
    unittest.main()
