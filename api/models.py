import datetime
import re


class Order:
    """Class will contain all my parcel orders"""

    def __init__(self, *args):
        self.destination = args[0]
        self.price = args[1]
        self.weihgt = args[2]
        self.Pickup_location = args[3]
        self.id = args[4]

    

class User:
    """Class handles users of the SendIT app"""
    users = []
    def __init__(self, username, email, password, admin='false'):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin
