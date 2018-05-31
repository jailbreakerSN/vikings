from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app import db
from app.auth import auth
from app.auth.forms import LoginForm, RegistrationForm
from app.models import utilisateurs


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        utilisateur = utilisateurs(email=form.email.data,
                                   username=form.username.data,
                                   firstname=form.firstname.data,
                                   lastname=form.lastname.data,
                                   password=form.password.data)

        # add employee to the database
        db.session.add(utilisateur)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        # return "Registration succeded!!!"
        return redirect(url_for('auth.login'))
    else:
        print("Formulaire invalide")
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)

    # load registration template
    return render_template('auth/vikings-signup.html', form=form, title='Inscription')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        utilisateur = utilisateurs.query.filter_by(email=form.email.data).first()
        if utilisateur is not None and utilisateur.check_password(form.password.data):
            # log employee in
            login_user(utilisateur, remember=form.rememberme.data)

            # redirect to the dashboard page after login
            # return "Login Success"
            return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/vikings-login.html', form=form, title='Connexion')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))
