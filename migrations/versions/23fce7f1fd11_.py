"""empty message

Revision ID: 23fce7f1fd11
Revises: 0e8d6b55b751
Create Date: 2017-08-16 15:37:22.371758

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '23fce7f1fd11'
down_revision = '0e8d6b55b751'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.Column('register_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('password', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('register_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###