from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import Utilisateur


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
        if Utilisateur.query.filter_by(email=field.data).first():
            raise ValidationError('Vous avez déjà un compte enregistré avec cet email!!!')

    def validate_username(self, field):
        if Utilisateur.query.filter_by(username=field.data).first():
            raise ValidationError('Ce nom d\'utilisateur est déjà utilisé!!!')


class estCreeForm(FlaskForm):
    idUtilisateur = StringField('Identifiant de l\'Utilisateur', validators=[DataRequired()])
    idProjet = StringField('Identifiant du Projet', validators=[DataRequired()])


class newProjectForm(FlaskForm):
    """
        Form for users to create new Project
    """
    nomProjet = StringField('Nom du Projet', validators=[DataRequired()])
    descriptionProjet = TextAreaField('Description du Projet', validators=[DataRequired()])
    nomWorkFlow = StringField('Nom du WorkFlow', validators=[DataRequired()])
    descriptionWorkFlow = TextAreaField('Description du WorkFlow', validators=[DataRequired()])

    submit = SubmitField('Enregistrer')
