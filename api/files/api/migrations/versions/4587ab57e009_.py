"""empty message

Revision ID: 4587ab57e009
Revises: c7167c13ff0d
Create Date: 2016-07-22 12:11:37.464492

"""

# revision identifiers, used by Alembic.
revision = '4587ab57e009'
down_revision = 'c7167c13ff0d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('google_cloud_billing_measurement')
    op.drop_table('google_cloud_billing_record')
    op.drop_table('google_cloud_billing_file')
    op.add_column('google_cloud_identity', sa.Column('last_fetched', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('google_cloud_identity', 'last_fetched')
    op.create_table('google_cloud_billing_record',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_file', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('start', mysql.DATETIME(), nullable=False),
    sa.Column('end', mysql.DATETIME(), nullable=False),
    sa.Column('item', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('cost', mysql.DECIMAL(precision=15, scale=6), nullable=False),
    sa.Column('currency', mysql.VARCHAR(length=3), nullable=False),
    sa.ForeignKeyConstraint(['id_file'], [u'google_cloud_billing_file.id'], name=u'google_cloud_billing_record_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('google_cloud_billing_file',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_bucket', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=224), nullable=False),
    sa.Column('md5', mysql.TINYBLOB(), nullable=False),
    sa.Column('media_link', mysql.VARCHAR(length=1023), nullable=False),
    sa.ForeignKeyConstraint(['id_bucket'], [u'google_cloud_billing_bucket.id'], name=u'google_cloud_billing_file_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('google_cloud_billing_measurement',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_record', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('measurement', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('sum', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('unit', mysql.VARCHAR(length=63), nullable=False),
    sa.ForeignKeyConstraint(['id_record'], [u'google_cloud_billing_record.id'], name=u'google_cloud_billing_measurement_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
