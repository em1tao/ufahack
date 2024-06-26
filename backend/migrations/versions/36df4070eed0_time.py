"""time

Revision ID: 36df4070eed0
Revises: 6cc903c554d6
Create Date: 2024-05-16 01:39:07.958805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '36df4070eed0'
down_revision: Union[str, None] = '6cc903c554d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tournament', 'starts_at',
               existing_type=sa.DATE(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tournament', 'starts_at',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###
