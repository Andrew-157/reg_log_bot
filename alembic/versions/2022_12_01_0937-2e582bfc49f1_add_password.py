"""add password

Revision ID: 2e582bfc49f1
Revises: f741186c2dfa
Create Date: 2022-12-01 09:37:07.393988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e582bfc49f1'
down_revision = 'f741186c2dfa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('accounts', sa.Column(
        'password', sa.String(15), nullable=False))


def downgrade() -> None:
    op.drop_column('accounts', 'password')
