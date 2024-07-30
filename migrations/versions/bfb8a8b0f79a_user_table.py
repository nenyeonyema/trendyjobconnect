"""user table

Revision ID: bfb8a8b0f79a
Revises: 
Create Date: 2024-07-24 23:30:18.539949

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bfb8a8b0f79a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employer', schema=None) as batch_op:
        batch_op.alter_column('company_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('company_location',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('company_logo',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)

    with op.batch_alter_table('jobseeker', schema=None) as batch_op:
        batch_op.alter_column('first_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('profile_pic',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               nullable=True)
        batch_op.alter_column('current_position',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('jobseeker', schema=None) as batch_op:
        batch_op.alter_column('current_position',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('profile_pic',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('first_name',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    with op.batch_alter_table('employer', schema=None) as batch_op:
        batch_op.alter_column('company_logo',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('company_location',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
        batch_op.alter_column('company_name',
               existing_type=sa.String(length=150),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###