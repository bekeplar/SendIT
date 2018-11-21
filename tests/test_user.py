import unittest
from api import app
from flask import json, jsonify
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

        self.assertEqual(message['message'], 'Bekalaze3 has been registered succesfully.')

    def test_user_register_empty_name(self):
        user = {
            'username': '',
            'email': 'bekeplar@mail.com',
            'password': 'bekeplax'
        }
        response = self.test_client.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'name field can not be empty.')

    def test_user_register_empty_password(self):
        user = {
            'name': 'Bekalaze',
            'email': '',
            'password': 'bekeplax'
        }
        response = self.test_client.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'],
                         'The email must have mixed characters!') 

    def test_user_cannot_register_twice(self):
        user = {
            'name': 'Bekalaze',
            'email': 'bekeplar@mail.com',
            'password': 'bekeplax'
        }
        response = self.test_client.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'], 'Email already registered!')

    def test_email_cannot_register_twice(self):
        user = {
            'name': 'kalanzi',
            'email': 'bekeplar@mail.com',
            'password': 'bekeplax'
        }
        response = self.test_client.post(
            'api/v1/auth/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())

        self.assertEqual(message['message'], 'kalanzi has been registered succesfully.')
                        