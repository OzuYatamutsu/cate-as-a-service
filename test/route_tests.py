from unittest import TestCase, main
from app import app

class RouteTests(TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_can_get_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, '')

    def test_can_post_index(self):
        response = self.app.post('/', 'test')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, '')         


if __name__ == '__main__':
    main()
