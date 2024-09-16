from flask import Blueprint, request, jsonify
from app.services.migration_service import migrate_data
from flask_jwt_extended import jwt_required

bp = Blueprint('migration', __name__)

@bp.route('/migrate', methods=['POST'])
@jwt_required()
def migrate():
    source_db = request.json.get('source_db')
    target_db = request.json.get('target_db')
    result = migrate_data(source_db, target_db)
    return jsonify(result), 200