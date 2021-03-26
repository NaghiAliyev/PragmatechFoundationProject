"""butun sehifelerde olan table-larin ilkin veziyyetinin qurulmasi

Revision ID: 463d2aee4523
Revises: 
Create Date: 2021-03-24 19:05:58.659937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '463d2aee4523'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_page',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('about_page_principle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('about_page_statistic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contact_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('telephone', sa.String(length=100), nullable=True),
    sa.Column('e_mail', sa.String(length=100), nullable=True),
    sa.Column('working_time', sa.String(length=100), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('finished_project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('start_time', sa.String(length=100), nullable=True),
    sa.Column('finis_time', sa.String(length=100), nullable=True),
    sa.Column('area', sa.String(length=100), nullable=True),
    sa.Column('cost', sa.String(length=100), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('main_page_principle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('main_page_statistic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('on_going_project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('start_time', sa.String(length=100), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partner_slider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc_title', sa.String(length=100), nullable=True),
    sa.Column('desc_content', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_table('product')
    op.drop_table('partner_slider')
    op.drop_table('on_going_project')
    op.drop_table('main_page_statistic')
    op.drop_table('main_page_principle')
    op.drop_table('finished_project')
    op.drop_table('contact_information')
    op.drop_table('about_page_statistic')
    op.drop_table('about_page_principle')
    op.drop_table('about_page')
    # ### end Alembic commands ###