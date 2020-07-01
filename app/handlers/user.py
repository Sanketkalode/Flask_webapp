from flask_login import login_user

from app.exceptions import UserExists
from app.handlers.handler import UserHandler
from app.models import UserModel


def login(username,password):
    user = UserHandler.find_by_username(username)
    if user is not None and UserHandler.check_password(user.password, password):
        login_user(user, remember=True)
        return True
    return False


def register(username,password):
    user = UserHandler.find_by_username(username)
    if user is None:
        newUser = UserModel(username, password)
        UserHandler.save_to_db(newUser)
        login_user(newUser, remember=True)
        return True
    raise UserExists
