from flask import flash, render_template
from flask_login import login_required

from app import db
from app.models import utilisateur
from app.projet import projet
from app.projet.forms import RegistrationForm


@projet.route('/projets/nouveau')
@login_required
def nouveau():
    """
    Render the dashboard template on the /dashboard route
    """
    pageactiveP = "active-page active"
    form = RegistrationForm()
    if form.validate_on_submit():
        utilisateur1 = utilisateur(email=form.email.data,
                                   username=form.username.data,
                                   firstname=form.firstname.data,
                                   lastname=form.lastname.data,
                                   password=form.password.data)

        # add employee to the database
        db.session.add(utilisateur1)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return "Registration succeded!!!"
    else:
        print("Formulaire invalide")
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)
    return render_template('projet/accueilprojet.html', title="Projet", form=form, pageactive=pageactiveP)


@projet.route('/projets')
def dashboard():
    """
        Affichage de la page de creation d'un nouveau projet
    """

    cardclass = "success"
    pageactiveN = "active-page active"

    return render_template('projet/nouveauprojet.html', title="Nouveau Projet", cardclass=cardclass,
                           pageactive=pageactiveN)
