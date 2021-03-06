"""empty message

Revision ID: ea76df970007
Revises: 56d7e3a1a479
Create Date: 2018-06-05 14:31:45.837134

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ea76df970007'
down_revision = '56d7e3a1a479'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilisateur',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=20), nullable=True),
                    sa.Column('email', sa.String(length=20), nullable=True),
                    sa.Column('password', sa.String(length=255), nullable=True),
                    sa.Column('firstname', sa.String(length=20), nullable=True),
                    sa.Column('lastname', sa.String(length=20), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_foreign_key(None, 'est_cree_user', 'utilisateur', ['id_Utilisateur'], ['id'])
    op.create_foreign_key(None, 'est_cree_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'est_mene_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'est_mene_user', 'utilisateur', ['id_Utilisateur'], ['id'])
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
    op.drop_table('utilisateur')
    # ### end Alembic commands ###
