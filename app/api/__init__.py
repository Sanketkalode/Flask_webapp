from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)

from app.api import views
from app.api import token, auth, error
