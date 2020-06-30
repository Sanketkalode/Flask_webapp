from app import db
from app.exceptions import ItemNotFound, ItemExists
from app.handlers.handler import ItemHandler
from app.models import ItemModel


def insert(name, price, stock, username):
    if ItemHandler.find_by_name(name, username) is not None:
        raise ItemExists
    else:
        newitem = ItemModel(name, price, stock, username)
        ItemHandler.save_to_db(newitem)
        return True


def update_stock(name, stock, username):
    item = ItemHandler.find_by_name(name, username)
    if item is not None:
        item.stock = stock
        db.session.commit()
        return True
    raise ItemNotFound


def update_price(name, price, username):
    item = ItemHandler.find_by_name(name, username)
    if item is not None:
        item.price = price
        db.session.commit()
        return True
    raise ItemNotFound
