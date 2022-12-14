"""empty message

Revision ID: e943e4fe9641
Revises: 
Create Date: 2022-11-20 15:27:08.620109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e943e4fe9641'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ArticalInfo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('clicks', sa.Integer(), nullable=True),
    sa.Column('tags', sa.String(length=200), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('content', sa.Text(length=4294967295), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('comments', sa.Integer(), nullable=True),
    sa.Column('likes_uid', sa.Text(length=4294967295), nullable=False),
    sa.Column('collect_num', sa.Integer(), nullable=False),
    sa.Column('collection', sa.Text(length=4294967295), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CommentInfo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(length=4294967295), nullable=False),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('fa', sa.Integer(), nullable=True),
    sa.Column('artid', sa.Integer(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('toid', sa.Integer(), nullable=True),
    sa.Column('likes_uid', sa.Text(length=4294967295), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('EmailInfo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('vcode', sa.String(length=10), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('UserInfo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('vcode', sa.String(length=10), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('artical_num', sa.Integer(), nullable=True),
    sa.Column('headshot', sa.String(length=100), nullable=True),
    sa.Column('tempshot', sa.String(length=100), nullable=True),
    sa.Column('abstract', sa.Text(length=1024), nullable=False),
    sa.Column('collect_num', sa.Integer(), nullable=False),
    sa.Column('collection', sa.Text(length=4294967295), nullable=False),
    sa.Column('x', sa.Integer(), nullable=False),
    sa.Column('y', sa.Integer(), nullable=False),
    sa.Column('hor', sa.Integer(), nullable=False),
    sa.Column('ver', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserInfo')
    op.drop_table('EmailInfo')
    op.drop_table('CommentInfo')
    op.drop_table('ArticalInfo')
    # ### end Alembic commands ###
