from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class EtapeForm(FlaskForm):
    """
    Form for users to create new Step in current Project
    """
    nomEtape = StringField("Nom de l'Etape", validators=[DataRequired()])
    objectifEtape = TextAreaField("Objectifs", validators=[DataRequired()])
    importanceEtape = IntegerField("Niveau d'importance(%)", validators=[DataRequired()])
    idLangage = SelectField("Langage de programmation", coerce=int, validators=[DataRequired()])

    submit = SubmitField('Enregistrer')
