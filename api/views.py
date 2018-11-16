from flask import request, jsonify, Blueprint, json
from api.models import Order, User
import datetime
import uuid
import re

orders = []
users = []
blueprint = Blueprint('application', __name__)

@blueprint.route('/home')
def index():
    return jsonify({
                'message': 'Welcome to my SendIT web.'
            })

@blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        name = data.get('name')
        password = data.get('password')
        user = ValidUser(name, password)
        if not user.valid_name():
            return jsonify({
                'message': 'Enter a valid name.'
            }), 400
        elif not valid_password():
            return jsonify({
                'message': 'Enter a valid password.'
            }), 400
        else:
            return jsonify({
                'message':
                '{} has logged in.'.format(username)
            }), 200
    except ValueError:
            return jsonify({
                'message': 'Wrong login credentials.'
                }), 400
            

@blueprint.route('/orders', methods=['POST'])
def create_order():
    """
    Function adds a parcel delivery order to the parcel-order  list.
    
    """
    try:
        data = request.get_json()
        destination = data.get('destination')
        pickup_location = data.get('pickup_location')
        price = data.get('price')
        name = data.get('name')
        weight = data.get('weight')
        id = len(orders) + 1

        order = Order(name, price, weight, id, destination, pickup_location)

        if order.Valid_order() is False:
            return jsonify({
                'message': 'Please fill all input fields!'
            }), 400
        if not isinstance(price, int) or not isinstance(weight, int):
            return jsonify({
                'message':
                'The price and weight must be numbers please!'
            }), 400
        orders.append(order.__dict__)
        return jsonify({
            'order': order.__dict__,
            'message': 'Order created successfully!'
        }), 201
    except ValueError:
        return jsonify({
            'message': 'You are providing wrong inputs'
        }), 400


@blueprint.route('/orders', methods=['GET'])
def get_all_parcels():
    """
    function to enable a user fetch all his parcel orders
    :returns:
    The entire list of parcel from the parcels.
    """
    if len(orders) == 0:
        return jsonify({
            'message': 'You havent created any order yet!'
        }), 400
    return jsonify({
        'orders': orders
    }), 200


@blueprint.route('/orders/<int:id>', methods=['GET'])
def get_specific_parcel(id):
    """
    Function to enable a registered 
    user fetch a specific parcel details.
    
    :params:
    :returns:
    The parcel order given the right id.
    """
    try:
        if len(orders) == 0:
            return jsonify({
                'message': 'you have not yet created orders yet!'
            }), 404
        order = orders[id - 1]
        return jsonify({
            'order': order,
            'message': 'parcel successfully found!'
        }), 200
    except IndexError:
        return jsonify({
            'message': 'No such order in parcels!'
        }), 404


@blueprint.route('/orders/<int:id>', methods=['PUT'])
def cancel_parcel(id):
    """
    Function for a user to cancel a specific parcel.
    :params:
    :returns:
    Return message for successful cancellation.
    """
    try:
        id = int(id)
        if len(orders) == 0:
            return jsonify({
                'message': 'You have no parcel orders yet!'
            }), 400
        elif not self.id(id):
            return jsonify({
                'message': ' parcel not found!'
            }), 400
        for order in orders:
            if order['id'] == id:     
                orders.remove(order)
                return jsonify({
                    'message': 'Parcel cancelled successfully!'
                }), 200
    except ValueError:
        return jsonify({
            'message': 'parcel id should be a number!'
        }), 400


@blueprint.route('/users', methods=['POST'])
def signup():
    try:

        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        userId = uuid.uuid4()
        user = User(name, email, password, userId)

        if not name or name.isspace() or not isinstance(
                name, str):
            return jsonify({
                'message': 'Username field can not be empty.'
                }), 400

        if not email or not re.match(
                    r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return jsonify({
                'message':
                'The  email must be alphanumeric please!'
            }), 400
        elif len(password) > 4:
            return jsonify({
                'message': 
                'Password must be at least 4 characters.'
                }), 400

        user = User(name, email, password, userId)
        return jsonify({
            'message': '{} has been registered succesfully.'.format(name)
        }), 201
    except ValueError:
        return jsonify({
            'message': 'Please try again.'
            }), 400



@blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    Function to enable an admin 
    fetch parcel details by userId.
    :params:
    :returns:
    The user given the right user id.
    """
    try:
        if len(users) == 0:
            return jsonify({
                'message': 'There are no customers yet!'
            }), 404
        user = users[id - 1]
        return jsonify({
            'user': user,
            'message': 'user found successfully!'
        }), 200
    except IndexError:
        return jsonify({
            'message': 'No such user in users!'
        }), 404
        







