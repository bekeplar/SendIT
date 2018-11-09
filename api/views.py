from flask import request, jsonify, Blueprint, json
from api.models import Order
import datetime


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
        id = len(Order.orders) + 1

        Order = Order(name, price, weight, id, destination, pickup_location)

        if Order.valid_order() is False:
            return jsonify({
                'message': 'Please fill all input fields!'
            }), 400
        if not isinstance(price, int) or not isinstance(weight, int):
            return jsonify({
                'message': 'The price and weight must be numbers please!'
            }), 400
        Order.orders.append(Order.__dict__)
        return jsonify({
            'order': Order.__dict__,
            'message': 'Kudos Order created successfully wow!'
        }), 201
    except Exception:
        return jsonify({
            'message': 'You are providing wrong inputs'
        }), 400

