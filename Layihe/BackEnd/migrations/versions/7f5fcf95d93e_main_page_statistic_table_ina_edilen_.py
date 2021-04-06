"""main_page_statistic table-ina edilen elave

Revision ID: 7f5fcf95d93e
Revises: 5eb2b0b40633
Create Date: 2021-03-31 21:56:40.227537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f5fcf95d93e'
down_revision = '5eb2b0b40633'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('main_page_statistic', schema=None) as batch_op:
        batch_op.add_column(sa.Column('static_value', sa.String(length=100), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('main_page_statistic', schema=None) as batch_op:
        batch_op.drop_column('static_value')

    # ### end Alembic commands ###