from flask import request

from app.api import api_blueprint
from app.handlers.handler import UserHandler
from app.models import UserModel


@api_blueprint.route('/api/register',methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']

    user = UserHandler.find_by_username(username)
    if user is None:
        newUser = UserModel(username, password)
        UserHandler.save_to_db(newUser)
        return {'message': 'user created successfully'}, 200
    return {"message": "User exists"}, 404
