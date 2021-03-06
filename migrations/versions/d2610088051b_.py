"""empty message

Revision ID: d2610088051b
Revises: 55fec626ef6e
Create Date: 2018-06-05 12:38:11.227738

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'd2610088051b'
down_revision = '55fec626ef6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('est_mene_user',
                    sa.Column('id_Utilisateur', sa.Integer(), nullable=False),
                    sa.Column('id_Projet', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['id_Projet'], ['projet.id_Projet'], ),
                    sa.ForeignKeyConstraint(['id_Utilisateur'], ['utilisateur.id'], ),
                    sa.PrimaryKeyConstraint('id_Utilisateur', 'id_Projet')
                    )
    op.create_index(op.f('ix_est_mene_user_id_Projet'), 'est_mene_user', ['id_Projet'], unique=False)
    op.create_foreign_key(None, 'projet', 'workflow', ['workflow_id_workflow'], ['id_Workflow'])
    op.create_foreign_key(None, 'workflow', 'projet', ['projet_id_projet'], ['id_Projet'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workflow', type_='foreignkey')
    op.drop_constraint(None, 'projet', type_='foreignkey')
    op.drop_index(op.f('ix_est_mene_user_id_Projet'), table_name='est_mene_user')
    op.drop_table('est_mene_user')
    # ### end Alembic commands ###
