"""empty message

Revision ID: 1aede642c2a9
Revises: 
Create Date: 2019-06-08 16:01:15.873552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1aede642c2a9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('vouchers', sa.Column('is_pay', sa.Boolean(), nullable=True))
    op.add_column('vouchers', sa.Column('is_refund', sa.Integer(), nullable=True))
    op.add_column('vouchers', sa.Column('is_send', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vouchers', 'is_send')
    op.drop_column('vouchers', 'is_refund')
    op.drop_column('vouchers', 'is_pay')
    # ### end Alembic commands ###
