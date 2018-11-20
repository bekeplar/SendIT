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
            id=1,
            present_location='Namanve'


    
       
       
       
       
       
        
       

       
       