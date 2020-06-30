from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_babel import _,lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                       EqualTo('password')])
    submit = SubmitField(_l('Register'))


class InsertItem(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    price = StringField(_l('Price'), validators=[DataRequired()])
    stock = StringField(_l('Items in Stock'), validators=[DataRequired()])
    submit = SubmitField(_l('Insert Item'))


class UpdatePrice(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    price = StringField(_l('Price'), validators=[DataRequired()])
    submit = SubmitField(_l('Update Price'))


class UpdateStock(FlaskForm):
    name = StringField(_l('Name'), validators=[DataRequired()])
    stock = StringField(_l('Items in Stock'), validators=[DataRequired()])
    submit = SubmitField(_l('Update Stock'))
