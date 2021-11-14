"""empty message

Revision ID: ea6eb58df4e7
Revises: 5412bd6d5b8b
Create Date: 2021-11-13 19:05:50.994211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea6eb58df4e7'
down_revision = '5412bd6d5b8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rental', 'available_inventory')
    op.drop_column('rental', 'videos_checked_out_count')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('videos_checked_out_count', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('rental', sa.Column('available_inventory', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
