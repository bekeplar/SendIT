from flask import request, jsonify, Blueprint, json
from api.models import Order
from api.validate import  ValidUser
import datetime

orders = []
blueprint = Blueprint('application', __name__)


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
                'message': 'The price and weight must be numbers please!'
            }), 400
        orders.append(order.__dict__)
        return jsonify({
            'order': order.__dict__,
            'message': 'Kudos Order created successfully wow!'
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

