"""empty message

Revision ID: 121c79a01bf7
Revises: fdc8cf89b52d
Create Date: 2018-06-05 13:41:38.167034

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '121c79a01bf7'
down_revision = 'fdc8cf89b52d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'est_cree_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'est_cree_user', 'utilisateur', ['id_Utilisateur'], ['id'])
    op.create_foreign_key(None, 'est_mene_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'est_mene_user', 'utilisateur', ['id_Utilisateur'], ['id'])
    op.create_foreign_key(None, 'etape', 'workflow', ['id_Workflow'], ['id_Workflow'])
    op.create_foreign_key(None, 'etape', 'langage', ['id_Langage'], ['id_Langage'])
    op.create_foreign_key(None, 'projet', 'workflow', ['workflow_id_workflow'], ['id_Workflow'])
    op.create_foreign_key(None, 'variable_env', 'etape', ['id_Etape'], ['id_Etape'])
    op.create_foreign_key(None, 'workflow', 'projet', ['projet_id_projet'], ['id_Projet'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workflow', type_='foreignkey')
    op.drop_constraint(None, 'variable_env', type_='foreignkey')
    op.drop_constraint(None, 'projet', type_='foreignkey')
    op.drop_constraint(None, 'etape', type_='foreignkey')
    op.drop_constraint(None, 'etape', type_='foreignkey')
    op.drop_constraint(None, 'est_mene_user', type_='foreignkey')
    op.drop_constraint(None, 'est_mene_user', type_='foreignkey')
    op.drop_constraint(None, 'est_cree_user', type_='foreignkey')
    op.drop_constraint(None, 'est_cree_user', type_='foreignkey')
    # ### end Alembic commands ###
