"""empty message

Revision ID: d8b24aff7b7d
Revises: d2610088051b
Create Date: 2018-06-05 13:03:15.424634

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd8b24aff7b7d'
down_revision = 'd2610088051b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('est_cree_user',
                    sa.Column('id_Utilisateur', sa.Integer(), nullable=False),
                    sa.Column('id_Projet', sa.Integer(), nullable=False),
                    sa.Column('date_creation_est_Cree_User', sa.Date(), nullable=False),
                    sa.ForeignKeyConstraint(['id_Projet'], ['projet.id_Projet'], ),
                    sa.ForeignKeyConstraint(['id_Utilisateur'], ['utilisateur.id'], ),
                    sa.PrimaryKeyConstraint('id_Utilisateur', 'id_Projet', 'date_creation_est_Cree_User')
                    )
    op.create_index(op.f('ix_est_cree_user_id_Projet'), 'est_cree_user', ['id_Projet'], unique=False)
    op.create_index(op.f('ix_est_cree_user_id_Utilisateur'), 'est_cree_user', ['id_Utilisateur'], unique=False)
    op.create_table('etape',
                    sa.Column('id_Etape', sa.Integer(), nullable=False),
                    sa.Column('nom', sa.String(length=30), nullable=True),
                    sa.Column('objectif', sa.String(length=255), nullable=True),
                    sa.Column('importance', sa.Integer(), nullable=True),
                    sa.Column('code_Etape', sa.Text(), nullable=True),
                    sa.Column('valide_Etape', sa.Boolean(), nullable=True),
                    sa.Column('version_Etape', sa.String(length=30), nullable=True),
                    sa.Column('id_Langage', sa.Integer(), nullable=True),
                    sa.Column('id_Workflow', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['id_Langage'], ['langage.id_Langage'], ),
                    sa.ForeignKeyConstraint(['id_Workflow'], ['workflow.id_Workflow'], ),
                    sa.PrimaryKeyConstraint('id_Etape')
                    )
    op.create_index(op.f('ix_etape_id_Langage'), 'etape', ['id_Langage'], unique=False)
    op.create_index(op.f('ix_etape_id_Workflow'), 'etape', ['id_Workflow'], unique=False)
    op.create_table('langage',
                    sa.Column('id_Langage', sa.Integer(), nullable=False),
                    sa.Column('nom', sa.String(length=30), nullable=True),
                    sa.PrimaryKeyConstraint('id_Langage')
                    )
    op.create_table('variable_env',
                    sa.Column('id_Variable_Env', sa.Integer(), nullable=False),
                    sa.Column('libelle_Variable_Env', sa.String(length=30), nullable=True),
                    sa.Column('valeur_Variable_Env', sa.String(length=255), nullable=True),
                    sa.Column('id_Etape', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['id_Etape'], ['etape.id_Etape'], ),
                    sa.PrimaryKeyConstraint('id_Variable_Env')
                    )
    op.create_index(op.f('ix_variable_env_id_Etape'), 'variable_env', ['id_Etape'], unique=False)
    op.create_index(op.f('ix_est_mene_user_id_Utilisateur'), 'est_mene_user', ['id_Utilisateur'], unique=False)
    op.create_foreign_key(None, 'est_mene_user', 'projet', ['id_Projet'], ['id_Projet'])
    op.create_foreign_key(None, 'est_mene_user', 'utilisateur', ['id_Utilisateur'], ['id'])
    op.create_foreign_key(None, 'projet', 'workflow', ['workflow_id_workflow'], ['id_Workflow'])
    op.create_foreign_key(None, 'workflow', 'projet', ['projet_id_projet'], ['id_Projet'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workflow', type_='foreignkey')
    op.drop_constraint(None, 'projet', type_='foreignkey')
    op.drop_constraint(None, 'est_mene_user', type_='foreignkey')
    op.drop_constraint(None, 'est_mene_user', type_='foreignkey')
    op.drop_index(op.f('ix_est_mene_user_id_Utilisateur'), table_name='est_mene_user')
    op.drop_index(op.f('ix_variable_env_id_Etape'), table_name='variable_env')
    op.drop_table('variable_env')
    op.drop_table('langage')
    op.drop_index(op.f('ix_etape_id_Workflow'), table_name='etape')
    op.drop_index(op.f('ix_etape_id_Langage'), table_name='etape')
    op.drop_table('etape')
    op.drop_index(op.f('ix_est_cree_user_id_Utilisateur'), table_name='est_cree_user')
    op.drop_index(op.f('ix_est_cree_user_id_Projet'), table_name='est_cree_user')
    op.drop_table('est_cree_user')
    # ### end Alembic commands ###
