"""empty message

Revision ID: 00c6f6dcf512
Revises: 075861239388
Create Date: 2018-06-27 00:17:48.967107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c6f6dcf512'
down_revision = '075861239388'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255)))
    op.execute('UPDATE users SET password=email')
    op.alter_column('users', 'password', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###