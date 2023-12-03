"""create rpn_calculations

Revision ID: 87d90d607cf5
Revises:
Create Date: 2023-12-02 11:22:50.402885

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87d90d607cf5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'rpn_calculations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('expression', sa.String(), nullable=False),
        sa.Column('time_executed', sa.DateTime, nullable=False),
        sa.Column('result', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table("rpn_calculations")
