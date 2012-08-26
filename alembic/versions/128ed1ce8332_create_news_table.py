"""create news table

Revision ID: 128ed1ce8332
Revises: None
Create Date: 2012-08-26 18:34:37.195828

"""

# revision identifiers, used by Alembic.
revision = '128ed1ce8332'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import functions


def upgrade():
    op.create_table(
        'news',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.Unicode(512), nullable=False),
        sa.Column('link', sa.Unicode(512)),
        sa.Column(
            'created_at', sa.DateTime(),
            default=functions.now(),
            index=True))


def downgrade():
    op.drop_table('news')
