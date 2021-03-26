"""PartnerSlider table-inda olan sehvin aradan qaldirilmasi

Revision ID: dec67c083cf4
Revises: fe6fd1ec6cf0
Create Date: 2021-03-25 19:10:07.997355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dec67c083cf4'
down_revision = 'fe6fd1ec6cf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('partner_slider', 'name',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('partner_slider', 'name',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
