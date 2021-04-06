"""davam eden layihelerle bagli olan hisselerin de elave olunmasi

Revision ID: 09099210d644
Revises: a12f3ad88d41
Create Date: 2021-04-06 20:09:47.826891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09099210d644'
down_revision = 'a12f3ad88d41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('on_going_project_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=100), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['on_going_project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('on_going_project', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('on_going_project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=100), nullable=True))

    op.drop_table('on_going_project_image')
    # ### end Alembic commands ###
