import unittest
from api import app
from flask import json, jsonify
from api.models import Order
from database.db import DatabaseConnection

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_create_order(self):
        """Test the method to add an order"""
        order = dict(
        destination='Mukono',
        date='23-11-2018',
        Pickup_location='Nakawa',
        price=80000,
        weight=75,
        name='Bekalaze',
        present_location='Namanve'
        )
        response = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(order)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)


    def test_create_order_with_empty_inputs(self):
        """Test the method to add an order"""
        order = dict(
        destination='',
        date='23-11-2018',
        Pickup_location='',
        price=80000,
        weight=75,
        name='',
        present_location='Namanve'
        )
        response = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(order)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)


    def test_create_new_order(self):
        user = {
            'name': 'Bekalaze',
            'password': 'bekeplax'
        }
        response = self.client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(user)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

        order = dict(

            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price=80000,
            weight=75,
            name='Bekalaze',
            present_location='Namanve'
        ) 
            
        response = self.client.post(
            'api/v1/orders',
            headers={'Authorization': 'Bearer ' + access_token['token']},
            content_type='application/json',
            data=json.dumps(order)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'], 'oredr created successfully.')    
     