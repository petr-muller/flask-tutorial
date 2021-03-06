"""add language to posts

Revision ID: 16c9eec98173
Revises: 72a7c4216b39
Create Date: 2019-08-27 23:32:06.028341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16c9eec98173'
down_revision = '72a7c4216b39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
