import unittest
from api import app
from flask import json, jsonify
from api.models import Order
from database.db import DatabaseConnection

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.db = DatabaseConnection()   

    def login_user(self):
        """Helper method in logging in"""
        user = dict(
            name='Bekalaze',
            password='bekkkkkyt'
        )
        response = self.client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(user)
        )
        reply = json.loads(response.data.decode())
        return reply    
    def create_order(self):
        """Method to call when creating orders.""" 
        reply = self.login_user()
        token = reply ['token']
        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price='xxc',
            weight='nnn',
            name='Bekalaze',
            present_location='Namanve'
        )
        response = self.client.post(
            '/api/v1/parcels',
            content_type='application/json',
            data=json.dumps(order),
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

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
            '/api/v1/parcels',
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
            '/api/v1/parcels',
            content_type='application/json',
            data=json.dumps(order)
        )
        access_token = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)


    def test_can_create_new_order_if_user(self):
        user = {
            'name': 'Bekalaze',
            'password': 'bekeplax'
        }
        response = self.client.post(
            'api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(user)
        )
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
            'api/v1/parcels',
            content_type='application/json',
            data=json.dumps(order)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 401)  

    def test_create_new_order(self):
        """Test that a user can create a parcel"""
        reply = self.login_user()
        token = reply['token']

        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price='xxc',
            weight='nnn',
            name='Bekalaze',
            present_location='Namanve'
        )
        response = self.client.post(
            '/api/v1/parcels',
            content_type='application/json',
            data=json.dumps(order),
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'Missing input fields!.')
        

    def test_create_order_missing_fields(self):
        """Test that empty fields are not allowed"""
        reply = self.login_user()
        token = reply['token']

        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price='xxc',
            weight='nnn',
            name='Bekalaze',
            present_location='Namanve'
        )
        response = self.client.post(
            '/api/v1/parcels',
            content_type='application/json',
            data=json.dumps(order),
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'],'Missing input fields!.')
        self.assertEqual(response.status_code, 400)

    def test_price_must_be_number(self):
        """Test that a price must be a number"""
        reply = self.login_user()
        token = reply['token']

        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price='xxc',
            weight='nnn',
            name='Bekalaze',
            present_location='Namanve'
        )
        response = self.client.post(
            '/api/v1/parcels',
            content_type='application/json',
            data=json.dumps(order),
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'],
                         'Missing input fields!.')
        self.assertEqual(response.status_code, 400)

    def test_get_all_parcels(self):
        """Test that a user can view all parcel his/her parcels."""
        reply = self.login_user()
        token = reply['token']

        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price=80000,
            weight=75,
            name='Bekalaze',
            present_location='Namanve'
        )

        response = self.client.get(
            '/api/v1/parcels',
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
        

    def test_get_all_parcels_from_empty_list(self):
        """Test that a user cannot get parcel records from an empty list"""
        reply = self.login_user()
        token = reply['token']

        response = self.client.get(
            '/api/v1/parcels',
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'You havent created any order yet!')
        self.assertEqual(response.status_code, 404)

    def test_get_specific_parcel(self):
        """Test that user can view a given parcel by id"""
        reply = self.login_user()
        token = reply['token']
        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price=80000,
            weight=75,
            name='Bekalaze',
            present_location='Namanve'
        )
        response = self.client.get(
            '/api/v1/parcels/1',
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'you have no such order!')
        self.assertEqual(response.status_code, 404)

    def test_get_specific_parcel_which_does_exist(self):
        """Test that a user cannot view  a non existing parcel"""
        reply = self.login_user()
        token = reply['token']

        reply = self.create_order()

        response = self.client.get(
            '/api/v1/parcels/2',
            headers={'Authorization': 'Bearer {}'.format(token)}
        )
        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'you have no such order!')
        self.assertEqual(response.status_code, 404)

    
    def test_get_specific_order_from_empty_list(self):
        """Test that a user cannot view a parcel from an empty list"""
        reply = self.login_user()

        self.assertEqual(reply['message'], 'Bekalaze has logged in.')
        token = reply['token']

        response = self.client.get(
            '/api/v1/parcels/1',
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'you have no such order!')
        self.assertEqual(response.status_code, 404)

    def test_get_order_from_empty_list(self):
        """Test that a user cannot view a parcel from an empty list"""
        reply = self.login_user()

        self.assertEqual(reply['message'], 'Bekalaze has logged in.')
        token = reply['token']

        response = self.client.get(
            '/api/v1/parcels/1',
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'you have no such order!')
        self.assertEqual(response.status_code, 404)


    def test_update_destination_of_non_existing(self):
        """Test that admin cannot update empty list"""
        reply = self.login_user()
        token = reply['token']

        order = dict(
            destination='Mukono',
            date='23-11-2018',
            Pickup_location='Nakawa',
            price=80000,
            weight=75,
            name='Bekalaze',
            present_location='Namanve'
        )

        response = self.client.put(
            '/api/v1/parcels/8/destination',
            content_type='application/json',
            data=json.dumps(order),
            headers={'Authorization': 'Bearer {}'.format(token)}
        )

        reply = json.loads(response.data.decode())

        self.assertEqual(reply['message'], 'you have no such order!')
        self.assertEqual(response.status_code, 404)

    def tearDown(self):
        self.client = app.test_client(self)
        self.db = DatabaseConnection()    

