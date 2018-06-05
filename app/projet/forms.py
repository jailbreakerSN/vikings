from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import utilisateurs


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('Firsname', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_password', message="Les mots de passe doivent correspondre!!!")
    ])
    confirm_password = PasswordField('Confirm Password')
    conditionDutilisation = BooleanField('J\'accepte les conditions!!')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if utilisateurs.query.filter_by(email=field.data).first():
            raise ValidationError('Vous avez déjà un compte enregistré avec cet email!!!')

    def validate_username(self, field):
        if utilisateurs.query.filter_by(username=field.data).first():
            raise ValidationError('Ce nom d\'utilisateur est déjà utilisé!!!')
