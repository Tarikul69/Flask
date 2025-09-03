from flask import Blueprint, jsonify, render_template, request
from .models import User
from .extensions import db

main = Blueprint("main", __name__)

#########################################################
##################Basic Crud Operation###################
@main.route("/", methods=["GET"])
def home():
    return render_template("index.html")

#########################################################
@main.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

#########################################################
@main.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()
    user = User(name=data["name"], email=data["email"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added!"}), 201
#########################################################
@main.route("/user_list", methods=["GET"])
def users():
    data = User.query.all()
    return jsonify({"data": data})