"""created at

Revision ID: d4de1e6ac3d1
Revises: 2e582bfc49f1
Create Date: 2022-12-01 09:43:50.464554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4de1e6ac3d1'
down_revision = '2e582bfc49f1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'accounts', sa.Column('created_at', sa.Date(),
                              nullable=False)
    )


def downgrade() -> None:
    op.drop_column('accounts', 'created_at')
