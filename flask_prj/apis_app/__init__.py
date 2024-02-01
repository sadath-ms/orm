# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_prj.config import Config


# apis_app = Flask(__name__)
# apis_app.config.from_object(Config)
# db = SQLAlchemy(apis_app)


# from apis_app.routes.auth.views import auth_blueprint




# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create an SQLAlchemy database instance
db = SQLAlchemy()

# Create a Flask-Migrate instance
migrate = Migrate()
from config import Config

def create_app(config=None):
    # Create the Flask app instance
    apis_app = Flask(__name__)

    # Load default configuration
    apis_app.config.from_object(Config)

    # Load configuration from a specified file if provided
    if config:
        apis_app.config.from_pyfile(Config)

    # Initialize extensions
    db.init_app(apis_app)
    migrate.init_app(apis_app, db)

    # Register blueprints and other components
    from apis_app.routes.auth.views import auth_blueprint
    apis_app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return apis_app

