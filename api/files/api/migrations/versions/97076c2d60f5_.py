"""empty message

Revision ID: 97076c2d60f5
Revises: fd62ceaa257c
Create Date: 2016-06-01 02:28:53.547760

"""

# revision identifiers, used by Alembic.
revision = '97076c2d60f5'
down_revision = 'fd62ceaa257c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lost_password', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'lost_password')
    ### end Alembic commands ###
