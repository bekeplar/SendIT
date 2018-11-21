import unittest
from api import app
from flask import json, jsonify
from api.models import Order


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)     