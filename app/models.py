import base64
import os
from datetime import datetime, timedelta

from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from flask import url_for
from app import db, login


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    price = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    user = db.Column(db.String(80))
    language = db.Column(db.String(5))

    def __init__(self, name, price, stock, user_id):
        self.name = name
        self.price = price
        self.stock = stock
        self.user = user_id

    def __repr__(self):
        return '<Item {}>'.format(self.body)

    @staticmethod
    def to_dict(items):
        data = []
        for item in items:
            data.append({'name': item.name,
                         'price': item.price,
                         'stock': item.stock})
        return data


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = UserModel.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user


@login.user_loader
def load_user(username):
    return UserModel.query.get(username)
