from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp

class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(message="Username is required."),
            Length(min=4, max=50, message="Username must be between 4 and 50 characters."),
            Regexp(
                r'^[A-Za-z0-9_]+$',
                message="Username must contain only letters, numbers, or underscores."
            )
        ]
    )

    email = StringField(
        "Email",
        validators=[
            InputRequired(message="Email is required."),
            Email(message="Enter a valid email address."),
            Length(max=100, message="Email must be less than 100 characters.")
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(message="Password is required."),
            Length(min=6, message="Password must be at least 6 characters."),
            Regexp(
                r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$',
                message="Password must include both letters and numbers."
            )
        ]
    )

    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            InputRequired(message="Email is required."),
            Email(message="Enter a valid email address."),
            Length(max=100, message="Email must be less than 100 characters.")
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            InputRequired(message="Password is required."),
            Length(min=6, message="Password must be at least 6 characters.")
        ]
    )

    submit = SubmitField("Login")
