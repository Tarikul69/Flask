from flask import Blueprint, flash, jsonify, redirect, render_template, request, session
from werkzeug.security import check_password_hash
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

#########################################################
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            # Store user in session
            session["user_id"] = user.id
            flash("Login successful!", "success")
            return redirect("about")
        else:
            flash("Invalid email or password.", "danger")
            return redirect("/")

