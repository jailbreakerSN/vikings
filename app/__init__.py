# third-party imports
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

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
    from app.projet import projet as projet_blueprint
    app.register_blueprint(projet_blueprint)
    from app.documentation import documentation as documentation_blueprint
    app.register_blueprint(documentation_blueprint)
    from app.etape import etape as etape_blueprint
    app.register_blueprint(etape_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    # @app.errorhandler(Exception)
    # def unhandled_exception(e):
    #     return render_template('errors/404_.html'), 404

    return app
