from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class utilisateurs(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(255))
    firstname = db.Column(db.String(20), unique=False)
    lastname = db.Column(db.String(20), unique=False)

    # def __init__(self, username, pwd):
    #     self.username = username
    #     self.password = pwd
    #
    def __init__(self, username, password, email, firstname, lastname):
        self.username = username
        self.password = generate_password_hash(password)
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return utilisateurs.query.get(int(user_id))