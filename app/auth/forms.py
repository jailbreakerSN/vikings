from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import Utilisateur


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField(id("email"), validators=[DataRequired(), Email()])
    username = StringField(id("username"), validators=[DataRequired()])
    firstname = StringField(id("firstname"), validators=[DataRequired()])
    lastname = StringField(id("lastname"), validators=[DataRequired()])
    password = PasswordField(id("password"), validators=[
        DataRequired(),
        EqualTo('confirm_password', message="Les mots de passe doivent correspondre!!!")
    ])
    confirm_password = PasswordField(id("confirm_password"))
    conditionDutilisation = BooleanField(id("aggree"))
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Utilisateur.query.filter_by(email=field.data).first():
            raise ValidationError('Vous avez déjà un compte enregistré avec cet email!!!')

    def validate_username(self, field):
        if Utilisateur.query.filter_by(username=field.data).first():
            raise ValidationError('Ce nom d\'utilisateur est déjà utilisé!!!')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField(id("email"), validators=[DataRequired(), Email()])
    password = PasswordField(id("password"), validators=[DataRequired()])
    rememberme = BooleanField(id("rememberme"))
    submit = SubmitField('Login')

    def validate_email(self, field):
        user = Utilisateur.query.filter_by(email=field.data).first()
        if not user:
            raise ValidationError('Adresse Email Invalide!!!')
    #
    # def validate_password(self, field):
    #     password = utilisateurs.query.filter_by(email=field.data).first()
    #     if not password:
    #         raise ValidationError("Mot de passe invalide!!!")
