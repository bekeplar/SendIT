import unittest
from api import app
from flask import json
from api.models import Order


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
        id=1
        )
        response = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(order)
        )
        reply = json.loads(response.data.decode())
        self.assertIn('Kudos Order created successfully wow!', reply['message'])


    def test_add_order_with_missing_inputs(self):
        """Testing whether missing input fields are not allowed"""
        order = dict(
            destination='',
            date='',
            Pickup_location='',
            price=80000,
            weight=75,
            name='Bekalaze',
            id=1
        )
        response = self.client.post(
            '/api/v1/orders',
            content_type='application/json',
            data=json.dumps(order)
        )
        reply = json.loads(response.data.decode())
        self.assertIn('Kudos Order created successfully wow!',reply['message'])
        

    def test_fetch_a_specific_order(self):
        """Test if a user can get a specific parcel"""
        response = self.client.get(
        '/api/v1/orders/1'  
        )
        reply = json.loads(response.data.decode())
        self.assertIn('parcel successfully found!',reply['message'])
        self.assertEqual(response.status_code, 200)    
        

    def test_fetch_an_existing_specific_order(self):
        """Test that a user can get an order which does  exist"""
        response = self.client.get(
        '/api/v1/orders/1'   
        )
        reply = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)


    def test_fetch_specific_order_from_empty_list(self):
        """Test that a user cannot get an order from an empty list"""
        response = self.client.get(
            '/api/v1/orders/1'
        )
        reply = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)        