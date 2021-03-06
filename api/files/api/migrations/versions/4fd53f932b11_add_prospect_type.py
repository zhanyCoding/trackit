"""add_prospect_type

Revision ID: 4fd53f932b11
Revises: e5a13efd803b
Create Date: 2017-07-24 15:25:25.487968

"""

# revision identifiers, used by Alembic.
revision = '4fd53f932b11'
down_revision = 'f35ff3668c49'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('prospect', sa.Column('type', sa.Unicode(length=25), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('prospect', 'type')
    ### end Alembic commands ###
