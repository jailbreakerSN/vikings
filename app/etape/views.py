from flask import render_template

from app.etape import etape


@etape.route('/projet/etape/details', methods=['GET', 'POST'])
def detailsetape():
    return render_template('etape/resultatsetape.html', title='Tutoriels')


@etape.route('/projet/etape/resultats', methods=['GET', 'POST'])
def resultatsetape():
    return render_template('etape/detailsetape.html', title='Informations')


@etape.route('/projet/etape/nouvelle', methods=['GET', 'POST'])
def nouvelle():
    return render_template('etape/nouvelle.html', title='Informations')
