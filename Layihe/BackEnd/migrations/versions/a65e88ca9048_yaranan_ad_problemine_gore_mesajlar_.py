"""yaranan ad problemine gore mesajlar table-nin adi deyisdirilir

Revision ID: a65e88ca9048
Revises: a0ad2a3ef7c1
Create Date: 2021-04-13 19:10:29.853680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a65e88ca9048'
down_revision = 'a0ad2a3ef7c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('full_name', sa.String(length=100), nullable=True),
    sa.Column('subject', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('message')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('full_name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('subject', sa.VARCHAR(length=100), nullable=True),
    sa.Column('content', sa.VARCHAR(length=100), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_message')
    # ### end Alembic commands ###