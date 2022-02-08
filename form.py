from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    """Form to register a new user"""

    username = StringField("Username",
        validators=[InputRequired()])

    password = PasswordField("Password",
        validators=[InputRequired()])

    email = EmailField("Email",
    validators=[InputRequired()])

    first_name = StringField("First Name",
        validators=[InputRequired()])

    last_name = StringField("Last Name",
        validators=[InputRequired()])
        

class LoginForm(FlaskForm):
    """Form to login a user"""

    username = StringField("Username",
        validators=[InputRequired()])

    password = PasswordField("Password",
        validators=[InputRequired()])