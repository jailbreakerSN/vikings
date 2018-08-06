from flask import Blueprint

etape = Blueprint('etape', __name__)

from app.etape import views
