from werkzeug.security import check_password_hash

from app import db
from app.models import ItemModel, UserModel


class ItemHandler:
    @classmethod
    def get_all(cls, user_id):
        return ItemModel.query.filter_by(user=user_id).all()

    @classmethod
    def find_by_name(cls, name, user_id):
        return ItemModel.query.filter_by(name=name).filter_by(user=user_id).first()

    @classmethod
    def save_to_db(cls, item):
        db.session.add(item)
        db.session.commit()

    @classmethod
    def commit(cls,item):
        db.session.commit(item)

    @classmethod
    def delete_from_db(cls, item):
        db.session.delete(item)
        db.session.commit()


class UserHandler:
    @classmethod
    def save_to_db(cls, user):
        db.session.add(user)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return UserModel.query.filter_by(username=username).first()

    @classmethod
    def check_password(cls,user_password, password):
        return check_password_hash(user_password, password)
