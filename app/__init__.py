from flask import Flask, render_template
from .config import Config
from .extensions import db, migrate
from .routes import main

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(main)

    return app
