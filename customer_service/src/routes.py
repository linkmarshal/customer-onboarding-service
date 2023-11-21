from flask import request, Blueprint, jsonify
from models import Customer, mongo
from bson import ObjectId


customer_bp = Blueprint('customer', __name__)
@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(**data)
    result = mongo.db.actor.insert_one(new_customer.__dict__)  # Insert into the 'actor' collection
    return jsonify({'message': 'Customer created', '_id': str(result.inserted_id)})

@customer_bp.route('/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    actor_collection = mongo.db.actor
    customer = actor_collection.find_one({'_id': ObjectId(customer_id)})

    if customer:
        # Return the customer details
        return jsonify({
            'first_name': customer['first_name'],
            'middle_name': customer['middle_name'],
            'last_name': customer['last_name'],
            'age': customer['age'],
            'nationality': customer['nationality'],
            'sex': customer['sex'],
            'income': customer['income'],
            'education_level': customer['education_level'],
            'position': customer['position']
        })
    else:
        return jsonify({'error': 'Customer not found'}, 404)

@customer_bp.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    # actor_collection = mongo.db.actor
    update_data = {key: value for key, value in data.items() if value is not None}  # Filter out None values
    actor_collection = mongo.db.actor
    result = actor_collection.update_one({'_id': ObjectId(customer_id)}, {'$set': update_data})
    if result.modified_count > 0:
        return jsonify({'message': 'Customer updated'})
    else:
        return jsonify({'error': 'Customer not found'}, 404)

@customer_bp.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    actor_collection = mongo.db.actor
    result = actor_collection.delete_one({'_id': ObjectId(customer_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Customer deleted'})
    else:
        return jsonify({'error': 'Customer not found'}, 404)
