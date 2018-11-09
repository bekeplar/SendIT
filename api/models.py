import datetime


class Order:
    """Class will contain all my parcel order objects"""
    Order = [
        {
            'destination': 'Mukono',
            'date': '23-11-2018',
            'Pickup_location': 'Nakawa',
            'price': 100000UGX,
            'weight': 100kg,
            '_id': 1111,
        }
    ]

    def __init__(self, *args):
        self.destination = args[0]
        self.price = args[1]
        self.weihgt = args[2]
        self._id = args[3]
        self.Pickup_location = args[4]
        self.id = args[5]

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