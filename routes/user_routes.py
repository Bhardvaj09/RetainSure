
from flask import Blueprint, request, jsonify
from services.user_service import get_users, get_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def health():
    return jsonify({"message": "User Management System"}), 200

@user_bp.route('/users', methods=['GET'])
def list_users():
    users = get_users()
    return jsonify([dict(user) for user in users]), 200

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_route(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(dict(user)), 200
    return jsonify({"error": "User not found"}), 404


