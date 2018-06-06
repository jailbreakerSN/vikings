from flask import Blueprint

documentation = Blueprint('documentation', __name__)

from app.documentation import views
