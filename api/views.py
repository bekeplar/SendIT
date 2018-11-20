from flask import Flask, request, jsonify, Blueprint, json
import uuid
import datetime
import re
from database.db import DatabaseConnection
from api.models import Order, User
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

blueprint = Blueprint('application', __name__)

db = DatabaseConnection()


@blueprint.route('/')
def home():
    return jsonify({
                'message': 'Welcome to my SendIT web.'
            })

@blueprint.route('/auth/signup', methods=['POST'])
def signup():
    try:

        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        userId = uuid.uuid4()
        password_hash = generate_password_hash(password, method='sha256')

        if not name or name.isspace() or not isinstance(
                name, str):
            return jsonify({
                'message': 'name field can not be empty.'
                }), 400

        if not email or not re.match(
                    r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return jsonify({
                'message':
                'The  email must be alphanumeric please!'
            }), 400
        elif len(password) < 4:
            return jsonify({
                'message': 
                'Password must be at least 4 characters.'
                }), 400
        name_db = db.check_name(name)
        email_db = db.check_email(email)
        if name_db != None:
            return jsonify({
                'message':
                'The name already has an account!'
            }), 400
        if email_db != None:
            return jsonify({
                'message':
                'Email already registered!'
            }), 400

        db.insert_user(name, email, password)      
        return jsonify({
            'message': '{} has been registered succesfully.'.format(name)
        }), 201
    except ValueError:
        return jsonify({
            'message': 'Please try again.'
            }), 400


@blueprint.route('/auth/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        name = data.get('name')
        password = data.get('password')
        
        if not name or name.isspace() or not isinstance(
                name, str):
            return jsonify({
                'message': 'Enter a valid name.'
            }), 400
        elif not password or password.isspace():
            return jsonify({
                'message': 'Enter a valid password.'
            }), 400
        user = db.login(name)
        access_token = create_access_token(identity=name)
        return jsonify({
            'token': access_token,
            'message':
            '{} has logged in.'.format(name)
        }), 200
    except ValueError:
            return jsonify({
                'message': 'provide correct credentials.'
                }), 400


@blueprint.route('/orders', methods=['POST'])
@jwt_required
def create_order():
    """
    Function adds a parcel delivery order to the database.
   
    """
    try:
        data = request.get_json()
        name = get_jwt_identity()

        destination = data.get('destination')
        Pickup_location = data.get('pickup_location')
        price = data.get('price')
        name = data.get('name')
        weight = data.get('weight')
        status = data.get('status')
        date = datetime.datetime.utcnow()
        present_location = data.get('present_location')

        order = Order(
            destination,
            price,
            weight,
            Pickup_location,
            name,
            status,
            date,
            present_location
            )

        if order.Valid_order() is False:
            return jsonify({
                'message': 'Please fill all input fields!'
            }), 400
        if not isinstance(price, int) or not isinstance(weight, int):
            return jsonify({
                'message':
                'The price and weight must be numbers please!'
            }), 400
        db.insert_order(destination, price, weight, Pickup_location,  name, status, present_location)
        return jsonify({
            'order': order.__dict__,
            'message': 'Order created successfully!'
        }), 201
    except ValueError:
        return jsonify({
            'message': 'Please provide right inputs'
        }), 400


@blueprint.route('/orders', methods=['GET'])
def get_all_parcels():
    """
    function to enable a user fetch all his parcel orders
    :returns:
    The entire list of parcel from the parcels database.
    """
    parcels_db = db.fetch_all_orders()
    if not parcels_db:
        return jsonify({
            'message': 'You havent created any order yet!'
        }), 400
    return jsonify({
        'orders': parcels_db
    }), 201


@blueprint.route('/orders/<int:id>', methods=['GET'])
@jwt_required
def get_specific_parcel(id):
    """
    Function to enable a registered
    user fetch a specific parcel details.
    :params:
    :returns:
    The parcel order given the right id.
    """
    name = get_jwt_identity()
    try:
        db = DatabaseConnection()
        order = db.fetch_order(id)
        if not order:
            return jsonify({
                'message': 'you have no such order!'
            }), 404
        return jsonify({
            'order': order,
            'message': 'parcel successfully found!'
        }), 200
    except TypeError:
        return jsonify({
            'message': 'Parcel id should be a number'
        }), 404


@blueprint.route('/orders/<int:id>', methods=['PUT'])
@jwt_required
def cancel_parcel(id):
    """
    Function for a user to cancel a specific parcel.
    :params:
    :returns:
    Return message for successful cancellation.
    """
    name = get_jwt_identity()
    try:
        db = DatabaseConnection()
        order = db.fetch_order(id)
        if not order:
            return jsonify({
                'message': 'you have no such order!'
            }), 404
        else:
            cancel_parcel = db.update_status(id,)
            return jsonify({
            'order': order,
            'message': 'parcel successfully cancelled!'
        }), 200
    except ValueError:
        return jsonify({
            'message': 'parcel id should be a number!'
        }), 400


