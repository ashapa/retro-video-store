"""empty message

Revision ID: 5412bd6d5b8b
Revises: d6a862608d8f
Create Date: 2021-11-13 12:01:33.232375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5412bd6d5b8b'
down_revision = 'd6a862608d8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rental', sa.Column('available_inventory', sa.Integer(), nullable=True))
    op.add_column('rental', sa.Column('checked_in', sa.Boolean(), nullable=True))
    op.add_column('rental', sa.Column('videos_checked_out_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rental', 'videos_checked_out_count')
    op.drop_column('rental', 'checked_in')
    op.drop_column('rental', 'available_inventory')
    # ### end Alembic commands ###
