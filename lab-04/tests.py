import unittest
from main import app


class TestHelloWorldRoute(unittest.TestCase):
    """Test that the root route returns a simple "Hello, World!" message.
    """

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<p>Hello, World!</p>')


if __name__ == '__main__':
    unittest.main()