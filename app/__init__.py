# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

# local imports

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    # app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)
    moment = Moment(app)

    from app import models

    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from app.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
