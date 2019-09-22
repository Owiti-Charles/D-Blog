"""Create subscribers model

Revision ID: 88771ae6cac6
Revises: 49004cb711ae
Create Date: 2019-09-22 16:07:11.764624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88771ae6cac6'
down_revision = '49004cb711ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.drop_table('subscribers')
    # ### end Alembic commands ###