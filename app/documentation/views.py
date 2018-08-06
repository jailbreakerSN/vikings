from flask import render_template

from app.documentation import documentation


@documentation.route('/tutoriels', methods=['GET', 'POST'])
def tutoriel():
    return render_template('documentation/informations.html', title='Tutoriels')


@documentation.route('/informations', methods=['GET', 'POST'])
def informations():
    return render_template('documentation/tutoriels.html', title='Informations')
