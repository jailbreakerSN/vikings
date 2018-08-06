from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.models import EstCreeUser
from app.models import EstMeneUser
from app.models import Projet
from app.models import Utilisateur
from app.projet import projet
from app.projet.forms import newProjectForm


@projet.route('/projets/nouveau', methods=['GET', 'POST'])
@login_required
def nouveau():
    """
    Render the dashboard template on the /dashboard route
    """
    form = newProjectForm()
    if form.validate_on_submit():
        # workflow = Workflow(nom=form.nomWorkFlow.data, description=form.descriptionWorkFlow.data)
        nouveauProjet = Projet(nom=form.nomProjet.data, description_Projet=form.descriptionProjet.data)
        db.session.add(nouveauProjet)
        db.session.commit()

        leprojet = Projet.query.filter_by(nom=form.nomProjet.data,
                                          description_Projet=form.descriptionProjet.data).first_or_404()

        creationProjet = EstCreeUser(id_Utilisateur=current_user.id, id_Projet=leprojet.id_Projet)
        membreProjet = EstMeneUser(id_Utilisateur=current_user.id, id_Projet=leprojet.id_Projet)

        db.session.add(creationProjet)
        db.session.add(membreProjet)

        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('projet.detailsprojet', id_Projet=leprojet.id_Projet))
    else:
        print("Formulaire invalide")
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)
    return render_template('projet/nouveauprojet.html', title="Nouveau Projet", form=form)


@projet.route('/projets')
@login_required
def dashboard():
    """
        Affichage de la page de creation d'un nouveau projet
    """

    cardclass = "success"

    mesProjets = Projet.query.join(Utilisateur.projets).filter(Utilisateur.id == current_user.id).all()

    # admin = Projet.query.join(Utilisateur.projetAdmin).filter(Utilisateur.id == current_user.id).all()
    # print(admin)
    # mesProjets = Utilisateur.query.filter(Utilisateur.projets.any(id=current_user.id)).all()

    return render_template('projet/accueilprojet.html', title="Projets", cardclass=cardclass, projets=mesProjets)


@projet.route('/projets/detailsprojet/<int:id_Projet>')
@login_required
def detailsprojet(id_Projet):
    title = "Projets"
    projet = Projet.query.filter_by(id_Projet=id_Projet).first_or_404()
    projetAdmin = Utilisateur.query.join(Projet.projetAdmin).filter(Projet.id_Projet == projet.id_Projet).first_or_404()
    projetMembers = Utilisateur.query.join(Projet.projetMembers).filter(Projet.id_Projet == projet.id_Projet).all()
    # print(projetMembers)
    creationProjet = EstCreeUser.query.filter_by(projet=projet).first_or_404()

    return render_template('projet/detailsprojet.html', **locals())
