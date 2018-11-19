from flask import Flask, request, jsonify, Blueprint, json
import uuid, datetime, re
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
@jwt_required
def signup():
    try:

        data = request.get_json()

        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        userId = uuid.uuid4()
        password_hash = generate_password_hash(method='sha256')

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
        db = DatabaseConnection()
        name_db = db.check_name(name)
        email_db = check_email(email)
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

        db.insert_user(name, email, password, userId)
        access_token = create_access_token(name)        
        return jsonify({
            'access_token': access_token,
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
        db = DatabaseConnection()
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
        pickup_location = data.get('pickup_location')
        price = data.get('price')
        name = data.get('name')
        weight = data.get('weight')
        status = data.get('status')
        date = data.get('date')
        id = len(orders) + 1
        present_location = data.get('present_location')

        order = Order(
            destination, 
            price, 
            weight, 
            pickup_location, 
            id, 
            name, 
            status, 
            date
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
        db = DatabaseConnection
        db.insert_order()
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
    db = DatabaseConnection
    parcels_db = db.get_all_parcels()
    if parcels_db == None:
        return jsonify({
            'message': 'You havent created any order yet!'
        }), 400
    return jsonify({
        'orders': orders
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
        order = db.query_one(id)
        if order == None:
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


