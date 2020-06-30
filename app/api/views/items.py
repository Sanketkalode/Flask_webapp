from flask import jsonify, request

from app.exceptions import ItemNotFound, ItemExists
from app.handlers.items import update_stock, update_price, insert

from app.api import api_blueprint
from app.api.auth import token_auth
from app.handlers.handler import ItemHandler
from app.models import ItemModel


@api_blueprint.route('/api/items', methods=['POST'])
@token_auth.login_required
def get_all():
    item = ItemHandler.get_all(token_auth.current_user().username)
    data = ItemModel.to_dict(item)
    return jsonify(data)


@api_blueprint.route('/api/insert', methods=['POST'])
@token_auth.login_required
def insert():
    name = request.json['name']
    price = request.json['price']
    stock = request.json['stock']
    username = token_auth.current_user().username

    try:
        if insert(name, price, stock, username):
            return jsonify({'message': 'Item inserted'})
    except ItemExists:
        return jsonify({'message': 'Item Already Exists'})


@api_blueprint.route('/api/update_stock', methods=['PUT'])
@token_auth.login_required
def update_item_stock():
    name = request.json['name']
    stock = request.json['stock']
    username = token_auth.current_user().username
    try:
        if update_stock(name, stock, username):
            return jsonify({'message': 'Item stock Updated '})
    except ItemNotFound:
        return jsonify({'message': 'Item Not found'})


@api_blueprint.route('/api/update_price', methods=['PUT'])
@token_auth.login_required
def update_item_price():
    name = request.json['name']
    price = request.json['price']
    username = token_auth.current_user().username
    try:
        if update_price(name, price, username):
            return jsonify({'message': 'Item stock Updated '})
    except ItemNotFound:
        return jsonify({'message': 'Item Not found'})
