# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, Email, Regexp

# class RegisterForm(FlaskForm):
#     username = StringField(
#         "Username",
#         validators=[
#             InputRequired(message="Username is required."),
#             Length(min=4, max=50, message="Username must be between 4 and 50 characters."),
#             Regexp(
#                 r'^[A-Za-z0-9_]+$',
#                 message="Username must contain only letters, numbers, or underscores."
#             )
#         ]
#     )

#     email = StringField(
#         "Email",
#         validators=[
#             InputRequired(message="Email is required."),
#             Email(message="Enter a valid email address."),
#             Length(max=100, message="Email must be less than 100 characters.")
#         ]
#     )

#     password = PasswordField(
#         "Password",
#         validators=[
#             InputRequired(message="Password is required."),
#             Length(min=6, message="Password must be at least 6 characters."),
#             Regexp(
#                 r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$',
#                 message="Password must include both letters and numbers."
#             )
#         ]
#     )

#     submit = SubmitField("Register")


# class LoginForm(FlaskForm):
#     email = StringField(
#         "Email",
#         validators=[
#             InputRequired(message="Email is required."),
#             Email(message="Enter a valid email address."),
#             Length(max=100, message="Email must be less than 100 characters.")
#         ]
#     )

#     password = PasswordField(
#         "Password",
#         validators=[
#             InputRequired(message="Password is required."),
#             Length(min=6, message="Password must be at least 6 characters.")
#         ]
#     )

#     submit = SubmitField("Login")

# class UpdateAccountForm(FlaskForm):
#     username = StringField(
#         "Username",
#         validators=[
#             InputRequired(message="Username is required."),
#             Length(min=4, max=50),
#             Regexp(r'^[A-Za-z0-9_]+$', message="Only letters, numbers, and underscores allowed.")
#         ]
#     )

#     email = StringField(
#         "Email",
#         validators=[
#             InputRequired(message="Email is required."),
#             Email(),
#             Length(max=100)
#         ]
#     )

#     gender = SelectField(
#         "Gender",
#         choices=[('', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
#         validators=[Optional()]
#     )

#     age = IntegerField("Age", validators=[Optional()])
#     mobile = StringField("Mobile Number", validators=[Optional(), Length(max=15)])

#     submit = SubmitField("Update Profile")

#     class ChangePasswordForm(FlaskForm):
#     current_password = PasswordField(
#         "Current Password",
#         validators=[InputRequired()]
#     )
#     new_password = PasswordField(
#         "New Password",
#         validators=[
#             InputRequired(),
#             Length(min=6),
#             Regexp(
#                 r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$',
#                 message="Password must include both letters and numbers."
#             )
#         ]
#     )
#     confirm_password = PasswordField(
#         "Confirm New Password",
#         validators=[InputRequired()]
#     )

#     submit = SubmitField("Change Password")




from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, Email, Regexp, Optional

class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(message="Username is required."),
            Length(min=4, max=50, message="Username must be between 4 and 50 characters."),
            Regexp(r'^[A-Za-z0-9_]+$', message="Username must contain only letters, numbers, or underscores.")
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
            Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$', message="Password must include both letters and numbers.")
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


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(message="Username is required."),
            Length(min=4, max=50),
            Regexp(r'^[A-Za-z0-9_]+$', message="Only letters, numbers, and underscores allowed.")
        ]
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(message="Email is required."),
            Email(),
            Length(max=100)
        ]
    )
    gender = SelectField(
        "Gender",
        choices=[('', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        validators=[Optional()]
    )
    age = IntegerField("Age", validators=[Optional()])
    mobile = StringField("Mobile Number", validators=[Optional(), Length(max=15)])
    submit = SubmitField("Update Profile")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[InputRequired()])
    new_password = PasswordField(
        "New Password",
        validators=[
            InputRequired(),
            Length(min=6),
            Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*?&]{6,}$', message="Password must include both letters and numbers.")
        ]
    )
    confirm_password = PasswordField("Confirm New Password", validators=[InputRequired()])
    submit = SubmitField("Change Password")
