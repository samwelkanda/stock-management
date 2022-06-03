"""Initial

Revision ID: fc5b45e021f5
Revises: fb07adc7d983
Create Date: 2022-06-03 18:50:00.102115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc5b45e021f5'
down_revision = 'fb07adc7d983'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'stock',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('count', sa.Integer)
    )


def downgrade() -> None:
    op.drop_table('stock')
