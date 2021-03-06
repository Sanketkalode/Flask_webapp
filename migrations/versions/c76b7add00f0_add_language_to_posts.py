"""add language to posts

Revision ID: c76b7add00f0
Revises: cddbbfb3bb4a
Create Date: 2020-06-26 13:46:58.309010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c76b7add00f0'
down_revision = 'cddbbfb3bb4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'language')
    # ### end Alembic commands ###
