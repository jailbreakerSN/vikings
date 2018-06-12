"""empty message

Revision ID: 56d7e3a1a479
Revises: 121c79a01bf7
Create Date: 2018-06-05 13:42:38.789134

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '56d7e3a1a479'
down_revision = '121c79a01bf7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'est_cree_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'est_cree_user', 'utilisateur', ['id_Utilisateur'], ['id'])
    op.create_foreign_key(None, 'est_mene_user', 'utilisateur', ['id_Utilisateur'], ['id'])
    op.create_foreign_key(None, 'est_mene_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'etape', 'langage', ['id_Langage'], ['id_Langage'])
    op.create_foreign_key(None, 'etape', 'workflow', ['id_Workflow'], ['id_Workflow'])
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