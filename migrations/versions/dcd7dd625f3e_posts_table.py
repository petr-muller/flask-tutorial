"""posts table

Revision ID: dcd7dd625f3e
Revises: c064a40e1d4a
Create Date: 2018-07-24 11:57:33.916468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "dcd7dd625f3e"
down_revision = "c064a40e1d4a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "post",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.String(length=140), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_post_timestamp"), "post", ["timestamp"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_post_timestamp"), table_name="post")
    op.drop_table("post")
    # ### end Alembic commands ###
