"""add content to posts table

Revision ID: d144aad82e9a
Revises: bf4aca028b40
Create Date: 2023-11-04 17:30:16.146775

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd144aad82e9a'
down_revision: Union[str, None] = 'bf4aca028b40'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
