from flask import render_template, redirect, url_for

from app import db
from app.etape import etape
from app.etape.form import EtapeForm
from app.models import Etape
from app.models import Langage


@etape.route('/projet/etape/details', methods=['GET', 'POST'])
def detailsetape():
    return render_template('etape/resultatsetape.html', title='Tutoriels')


@etape.route('/projet/etape/resultats', methods=['GET', 'POST'])
def resultatsetape():
    return render_template('etape/detailsetape.html', title='Informations')


@etape.route('/projet/<int:id_Projet>/etape/nouvelle', methods=['GET', 'POST'])
def nouvelle(id_Projet):
    form = EtapeForm()
    idlangages = [(l.id_Langage, l.nom) for l in Langage.query.all()]
    form.idLangage.choices = idlangages
    if form.validate_on_submit():
        nouvelleEtape = Etape(nom=form.nomEtape.data, objectif=form.objectifEtape.data,
                              importance=form.importanceEtape.data, id_Langage=form.idLangage.data, id_Projet=id_Projet)
        db.session.add(nouvelleEtape)
        db.session.commit()
        return redirect(url_for('projet.detailsprojet', id_Projet=id_Projet))
    return render_template('etape/nouvelle.html', title='Nouvelle Etape', form=form)
