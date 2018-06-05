from flask import render_template

from app.errors import errors


@errors.route('/erreur')
def page_not_found():
    # note that we set the 404 status explicitly
    return render_template('errors/404.html'), 404
