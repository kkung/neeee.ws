"""add score

Revision ID: 591171d13c3f
Revises: 128ed1ce8332
Create Date: 2012-08-26 21:47:01.212820

"""

# revision identifiers, used by Alembic.
revision = '591171d13c3f'
down_revision = '128ed1ce8332'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('news', sa.Column('votes', sa.Integer, default=0))


def downgrade():
    op.add_column('news', 'votes')
