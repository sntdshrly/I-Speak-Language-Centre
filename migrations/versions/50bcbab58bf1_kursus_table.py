"""kursus table

Revision ID: 50bcbab58bf1
Revises: 
Create Date: 2021-12-11 11:54:10.352261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '50bcbab58bf1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kursus')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kursus',
    sa.Column('idKursus', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('namaKursus', mysql.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('idKursus'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
