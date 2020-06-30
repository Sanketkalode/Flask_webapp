from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from app.api.error import error_response
from app.handlers.handler import UserHandler
from app.models import UserModel

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    user = UserHandler.find_by_username(username)
    if user and UserHandler.check_password(user.password, password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)


@token_auth.verify_token
def verify_token(token):
    return UserModel.check_token(token) if token else None


@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)
