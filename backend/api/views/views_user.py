from flask import Blueprint, request, jsonify, session
from api.models import db, User
from api.extensions import db, cache  # Import from extensions.py

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']  # In a real-world scenario, I'd hash this
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.json()), 201

@user_blueprint.route('/login', methods=['POST'])
@cache.cached(timeout=50)  # cache for 50 seconds
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:  # Again, in a real-world scenario, I'd hash and check the password
        session['logged_in'] = True
        session['user_id'] = user.userID
        return jsonify({"message": "Logged in successfully!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@user_blueprint.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully!"}), 200
