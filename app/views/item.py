from flask import render_template
from flask_login import current_user, login_required

from app.exceptions import ItemExists, ItemNotFound
from app.forms import InsertItem, UpdatePrice, UpdateStock
from app.handlers.items import  update_price, update_stock, insert
from app.views import main_blueprint
from app.handlers.handler import ItemHandler


@login_required
@main_blueprint.route('/items', methods=['GET'])
def get_items():
    item = ItemHandler.get_all(current_user.username)
    return render_template('items.html', item=item)


@login_required
@main_blueprint.route('/item/<item>', methods=['GET'])
def get_item():
    item = ItemHandler.find_by_name()
    return render_template('items.html', item=item)


@login_required
@main_blueprint.route('/item', methods=['POST', 'GET'])
def insert_item():
    form = InsertItem()
    try:
        if form.validate_on_submit():
            if insert(form.name.data, form.price.data,form.stock.data, current_user.username):
                return render_template('dashboard.html')
    except ItemExists:
        render_template('exception.html',ex=4)
    return render_template('insert_item.html', title='Insert Item', form=form)


@login_required
@main_blueprint.route('/updateprice', methods=['POST', 'GET'])
def update_item_price():
    form = UpdatePrice()
    try:
        if form.validate_on_submit():
            if update_price(form.name.data,form.price.data,current_user.username):
                return render_template('dashboard.html')
    except ItemNotFound:
        render_template('exception.html',ex=3)
    return render_template('update_price.html', title='Update Item', form=form)


@login_required
@main_blueprint.route('/updatestock', methods=['POST', 'GET'])
def update_item_stock():
    form = UpdateStock()
    try:
        if form.validate_on_submit():
            if update_stock(form.name.data,form.stock.data,current_user.username):
                return render_template('dashboard.html')
    except ItemNotFound:
        render_template('exception.html', ex=3)
    return render_template('update_stock.html', title='Update Item', form=form)


# @login_required
# @main_blueprint.route('/delete')
# def delete():
#     item = ItemModel.get_items()
#     return render_template('/delete_item.html', item=item)
#
#
# @login_required
# @main_blueprint.route('/item/<name>', methods=['DELETE'])
# def delete_item(name):
#     item = ItemModel.find_by_name(name, current_user.username)
#     try:
#         if item is not None:
#             item.delete_from_db()
#             flash(_('Item deleted'))
#         else:
#             raise ItemNotFound
#     except ItemNotFound:
#         render_template('exception.html', ex=3)
#     return render_template('dashboard.html')
