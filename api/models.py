import datetime


class Order:
    """Class will contain all my parcel orders"""

    def __init__(self, *args):
        self.destination = args[0]
        self.price = args[1]
        self.weight = args[2]
        self.Pickup_location = args[3]
        self.name = args[4]
        self.status = args[5]
        self.date = args[6]
        self.present_location = args[7]


    def Valid_order(self):
        """
        Method validates the attributes of an order.
        : it should return:
        True - if the given order details are all valid.
        False - if one or all of the given details  are invalid.
        """
        if not self.destination or not self.price or not self.weight or\

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
    """Class will contain all my user objects"""

    def __init__(self, name, email, password, userId):


        self.name = name
        self.email = email
        self.password = password
        self.userId = userId
        self.admin = False


        




