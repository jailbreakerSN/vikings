from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class Utilisateur(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(40), unique=True)
    password = db.Column(db.String(255))
    firstname = db.Column(db.String(40), unique=False)
    lastname = db.Column(db.String(40), unique=False)

    projetAdmin = db.relationship('Projet', secondary='est_cree_user',
                                  backref=db.backref('projetAdmin', lazy='dynamic'))

    projetMembers = db.relationship('Projet', secondary='est_mene_user',
                                    backref=db.backref('projetMembers', lazy='dynamic'))

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


class Projet(db.Model):
    __tablename__ = 'projet'

    id_Projet = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30))
    description_Projet = db.Column(db.Text)
    workflow_id_workflow = db.Column(db.ForeignKey('workflow.id_Workflow'), index=True)

    workflow = db.relationship('Workflow', primaryjoin='Projet.workflow_id_workflow == Workflow.id_Workflow')
    utilisateur = db.relationship('Utilisateur', secondary='est_mene_user',
                                  backref=db.backref('projets', lazy='dynamic'))


class Workflow(db.Model):
    __tablename__ = 'workflow'

    id_Workflow = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30))
    description = db.Column(db.Text)
    projet_id_projet = db.Column(db.ForeignKey('projet.id_Projet'), index=True)

    projet = db.relationship('Projet', primaryjoin='Workflow.projet_id_projet == Projet.id_Projet')


# class EstMeneUser(db.Model):
#     __table_name__ = 'est_mene_user'
#     id_Utilisateur = db.Column(db.ForeignKey('utilisateur.id'), primary_key=True, nullable=False, index=True)
#     id_Projet = db.Column(db.ForeignKey('projet.id_Projet'), primary_key=True, nullable=False, index=True)
#
#     projet = db.relationship('Projet')
#     utilisateur = db.relationship('Utilisateur')
#
est_mene_user = db.Table(
    'est_mene_user', db.metadata,
    db.Column('id_Projet', db.ForeignKey('projet.id_Projet'), primary_key=True, nullable=False),
    db.Column('id_Utilisateur', db.ForeignKey('utilisateur.id'), primary_key=True, nullable=False,
              index=True)
)


class EstCreeUser(db.Model):
    __tablename__ = 'est_cree_user'

    id_Utilisateur = db.Column(db.ForeignKey('utilisateur.id'), primary_key=True, nullable=False, index=True)
    id_Projet = db.Column(db.ForeignKey('projet.id_Projet'), primary_key=True, nullable=False, index=True)
    date_creation_est_Cree_User = db.Column(db.Date, primary_key=True, nullable=False)

    projet = db.relationship('Projet')
    utilisateur = db.relationship('Utilisateur')


class Etape(db.Model):
    __tablename__ = 'etape'

    id_Etape = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30))
    objectif = db.Column(db.String(255))
    importance = db.Column(db.Integer)
    code_Etape = db.Column(db.Text)
    valide_Etape = db.Column(db.Boolean, default=False)
    version_Etape = db.Column(db.String(30), default='1.0')
    id_Langage = db.Column(db.ForeignKey('langage.id_Langage'), index=True)
    id_Workflow = db.Column(db.ForeignKey('workflow.id_Workflow'), index=True)

    langage = db.relationship('Langage')
    workflow = db.relationship('Workflow')


class Langage(db.Model):
    __tablename__ = 'langage'

    id_Langage = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30))


class VariableEnv(db.Model):
    __tablename__ = 'variable_env'

    id_Variable_Env = db.Column(db.Integer, primary_key=True)
    libelle_Variable_Env = db.Column(db.String(30))
    valeur_Variable_Env = db.Column(db.String(255))
    id_Etape = db.Column(db.ForeignKey('etape.id_Etape'), index=True)

    etape = db.relationship('Etape')


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))
