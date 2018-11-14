import datetime


class Order:
    """Class will contain all my parcel orders"""

    def __init__(self, *args):
        self.destination = args[0]
        self.price = args[1]
        self.weihgt = args[2]
        self.Pickup_location = args[3]
        self.id = args[4]
        self.name = args[5]

    def Valid_order(self):
        """
        Method validates the attributes of an order.
        : it should return:
        True - if the given order details are all valid.
        False - if one or all of the given details  are invalid.
        """
        if not self.destination or not self.price or not self.weihgt or\
                self.destination.isspace():
            return False
        else:
            return True

        if not self.Pickup_location or not self.id or not self.weihgt.isspace() or\
                self.destination.isspace():
            return False
        else:
            return True    
    

    

class User:
    """Class handles users of the SendIT app"""
    users = []
    def __init__(self, name, email, password, userId):
        self.name = name
        self.email = email
        self.password = password
        self.userId = userId

        



orders = [
    {
        'destination': 'Mukono',
        'date': '23-11-2018',
        'Pickup_location': 'Nakawa',
        'price': 80000,
        'weight': 75,
        'name': 'Bekalaze',
        'id': 1
    }
]