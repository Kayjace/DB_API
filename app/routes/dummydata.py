from flask import Blueprint, request, jsonify
from app.services.dummydata_service import generate_dummy_data, insert_dummy_data
from flask_jwt_extended import jwt_required

bp = Blueprint('dummydata', __name__)

@bp.route('/generate', methods=['POST'])
@jwt_required()
def generate_dummy():
    data = request.json
    result = generate_dummy_data(data)
    return jsonify(result), 200

@bp.route('/insert', methods=['POST'])
@jwt_required()
def insert_dummy():
    data = request.json
    result = insert_dummy_data(data)
    return jsonify(result), 200