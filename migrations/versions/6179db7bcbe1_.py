"""empty message

Revision ID: 6179db7bcbe1
Revises: 
Create Date: 2022-10-01 13:24:50.195208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6179db7bcbe1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitter', sa.String(length=250), nullable=True),
    sa.Column('fact', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('facts')
    # ### end Alembic commands ###
