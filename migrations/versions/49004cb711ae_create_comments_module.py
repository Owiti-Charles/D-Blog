"""Create comments module

Revision ID: 49004cb711ae
Revises: 20a6c34d6ac3
Create Date: 2019-09-22 15:23:13.249876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49004cb711ae'
down_revision = '20a6c34d6ac3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_post_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'blogs', ['blog_id'], ['id'])
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_post_id_fkey', 'comments', 'blogs', ['post_id'], ['id'])
    op.drop_column('comments', 'blog_id')
    # ### end Alembic commands ###