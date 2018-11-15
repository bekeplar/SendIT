import unittest
from api import app
from flask import json
from api.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)


    def test_signup(self):
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
        self.assertIn('Please try again.',reply['message'])   

    def test_login_with_missing_input(self):
        """Test the method to signup a user"""
        user = dict(
        name='',
        email= 'bekeplar@gmail.com',
        password= 'Beka@43'
        )
        response = self.client.post(
            '/api/v1/users',
            content_type='application/json',
            data=json.dumps(user)
        )
        reply = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)               


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
        self.assertEqual(response.status_code, 400)  

    def test_fetch_a_non_existing_specific_user(self):
        """Test that a non existing user can be obtained"""
        response = self.client.get(
        '/api/v1/orders/1122'   
        )
        reply = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404) 

    def test_name_already_exists(self):
        """Test an existing user"""
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
        self.assertEqual(response.status_code, 400)
        
           
