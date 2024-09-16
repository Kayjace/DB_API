from flask import Blueprint, jsonify
from app.services.request_service import get_schema, get_tables
from flask_jwt_extended import jwt_required

bp = Blueprint('request', __name__)

@bp.route('/schema', methods=['GET'])
@jwt_required()
def schema():
    result = get_schema()
    return jsonify(result), 200

@bp.route('/tables', methods=['GET'])
@jwt_required()
def tables():
    result = get_tables()
    return jsonify(result), 200