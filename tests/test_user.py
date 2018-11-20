import unittest
from api import app
from flask import json
from api.models import User


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_user_register(self):
        user = {
            'name': 'Bekalaze3',
            'email': 'bekeplar@gmal.com',
            'password': 'bekeplax'
        }
        response = self.test_client.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        print(json.loads(response.data.decode()))

        self.assertEqual(message['message'], 'Bekalaze3 has been registered succesfully.')
