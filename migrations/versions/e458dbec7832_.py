"""empty message

Revision ID: e458dbec7832
Revises: 441c8f070db9
Create Date: 2019-10-20 17:55:13.736622

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e458dbec7832'
down_revision = '441c8f070db9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show_items',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id')
    )
    op.drop_table('shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='shows_artist_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='shows_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id', name='shows_pkey')
    )
    op.drop_table('show_items')
    # ### end Alembic commands ###
