from flask import render_template, flash
from flask_login import current_user, login_user, logout_user
from flask_babel import _

from app.exceptions import UserExists
from app.forms import LoginForm, RegistrationForm
from app.handlers.handler import UserHandler
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
    if form.validate_on_submit():
        user = UserHandler.find_by_username(form.username.data)
        if user is not None and UserHandler.check_password(user.password, form.password.data):
            login_user(user, remember=True)
            return render_template('dashboard.html')
        flash(_('Invalid Username or Password'))
        return render_template('index.html')
    return render_template('login.html', title='Login', form=form)


@main_blueprint.route('/register', methods=['POST', 'GET'])
def user_register():
    form = RegistrationForm()
    user = UserHandler.find_by_username(form.username.data)
    try:
        if form.validate_on_submit():
            if user is None:
                newUser = UserModel(form.username.data, form.password.data)
                UserHandler.save_to_db(newUser)
                login_user(newUser, remember=True)
                return render_template('dashboard.html')
            else:
                raise UserExists
    except UserExists:
        render_template('exception.html', ex=2)
    return render_template('register.html', title='SignUp', form=form)


@main_blueprint.route('/logout')
def logout():
    logout_user()
    return render_template('index.html')
