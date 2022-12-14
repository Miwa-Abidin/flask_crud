"""empty message

Revision ID: 589d8119e6d0
Revises: 
Create Date: 2022-11-28 10:34:56.887506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '589d8119e6d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    # ### end Alembic commands ###
