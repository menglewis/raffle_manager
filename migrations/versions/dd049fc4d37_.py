"""empty message

Revision ID: dd049fc4d37
Revises: 7542466fa73
Create Date: 2014-05-10 18:43:58.875719

"""

# revision identifiers, used by Alembic.
revision = 'dd049fc4d37'
down_revision = '7542466fa73'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('raffle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('raffle_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('raffle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['raffle_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('raffle_entry')
    op.drop_table('raffle')
    ### end Alembic commands ###
