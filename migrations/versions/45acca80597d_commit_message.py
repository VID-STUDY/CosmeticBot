"""Commit message

Revision ID: 45acca80597d
Revises: 9a031d7f7df2
Create Date: 2020-09-12 10:34:50.278607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45acca80597d'
down_revision = '9a031d7f7df2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stats', sa.Column('dish_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stats', 'dish_id')
    # ### end Alembic commands ###
