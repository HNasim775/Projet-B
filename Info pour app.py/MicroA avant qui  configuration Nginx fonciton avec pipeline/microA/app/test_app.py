import unittest
import json
from app import app, db

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_to_cart(self):
        response = self.client.post(
            '/add_to_cart',
            data=json.dumps({'product_id': 1, 'quantity': 3}),
            content_type='application/json'
        )
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)
        self.assertIn('order_id', data)

if __name__ == '__main__':
    unittest.main()
