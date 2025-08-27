from flask import Blueprint, jsonify, request
from .models import User
from .extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Flask app is running!"})

@main.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added!"}), 201
