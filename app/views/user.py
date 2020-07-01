from flask import render_template, flash
from flask_login import current_user, login_user, logout_user
from flask_babel import _

from app.exceptions import UserExists
from app.forms import LoginForm, RegistrationForm
from app.handlers.handler import UserHandler
from app.handlers.user import login, register
from app.models import UserModel
from app.views import main_blueprint


@main_blueprint.route('/index')
@main_blueprint.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('dashboard.html')
    return render_template('index.html')


@main_blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@main_blueprint.route('/login', methods=['GET', 'POST'])
def user_login():
    if current_user.is_authenticated:
        return render_template('dashboard.html')
    form = LoginForm()
    username = form.username.data
    password = form.password.data
    if form.validate_on_submit():
        if login(username,password):
            return render_template('dashboard.html')
        return render_template('index.html')
    return render_template('login.html', title='Login', form=form)


@main_blueprint.route('/register', methods=['POST', 'GET'])
def user_register():
    form = RegistrationForm()
    username = form.username.data
    password = form.password.data
    user = UserHandler.find_by_username(form.username.data)
    try:
        if form.validate_on_submit():
            if register(username,password):
                return render_template('dashboard.html')
    except UserExists:
        render_template('exception.html', ex=2)
    return render_template('register.html', title='SignUp', form=form)


@main_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')
