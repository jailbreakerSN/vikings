from flask import render_template
from flask_login import login_required

from app.home import home


@home.route('/accueil')
@login_required
def dashboard():
    pageactive = "active-page active"
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/accueil.html', title="Accueil", pageactive=pageactive)
