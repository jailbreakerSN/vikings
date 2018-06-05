from flask import Blueprint

projet = Blueprint('projet', __name__)

from app.projet import views
