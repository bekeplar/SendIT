import unittest
from api import app
from flask import json
from api.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

def test_signup():
    """Test the method to signup a user"""
    user = dict(
    name='Bekalaze',
    email= 'bekeplar@gmail.com',
    password= 'Beka@43'
    )
    response = self.client.post(
        '/api/v1/users',
        content_type='application/json',
        data=json.dumps(user)
    )
    reply = json.loads(response.data.decode())
    self.assertIn('Bekalaze has been registered succesfully.')       


def test_register_empty_password(self):
    """Test the method to signup a user"""
    user = dict(
    name='Bekalaze',
    email= 'bekeplar@gmail.com',
    password= ''
    )
    response = self.client.post(
        '/api/v1/users',
        content_type='application/json',
        data=json.dumps(user)
    )
    reply = json.loads(response.data.decode())
    self.assertIn('Password must be at least 4 characters.')       

