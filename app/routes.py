from flask import Blueprint, jsonify, render_template, request
from .models import User
from .extensions import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Template</title>
</head>
<body>
    <center><h2>Welcome to my flask template</h2></center>
</body>
</html>"""

@main.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added!"}), 201

@main.route("/user_list", methods=["GET"])
def users():
    data = User.query.all()
    return jsonify({"data": data})