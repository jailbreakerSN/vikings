from flask import flash, render_template
from flask_login import login_required

from app.projet import projet
from app.projet.forms import RegistrationForm
from app.projet.forms import formProjet


@projet.route('/projets/nouveau')
@login_required
def nouveau():
    """
    Render the dashboard template on the /dashboard route
    """
    pageactiveP = "active-page active"
    form = RegistrationForm()

    projetForm = formProjet()
    if form.validate_on_submit():
        # db.session.add(utilisateur)
        # db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return "Registration succeded!!!"
    else:
        print("Formulaire invalide")
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)
    return render_template('projet/nouveauprojet.html', title="Nouveau Projet", form=projetForm)


@projet.route('/projets')
@login_required
def dashboard():
    """
        Affichage de la page de creation d'un nouveau projet
    """

    cardclass = "success"

    # mesProjets = Projet.query()

    return render_template('projet/accueilprojet.html', title="Projets", cardclass=cardclass)
