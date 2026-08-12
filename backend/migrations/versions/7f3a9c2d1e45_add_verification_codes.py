"""add verification codes and login attempts

Revision ID: 7f3a9c2d1e45
Revises: 201e8719b346
Create Date: 2026-08-12

邮箱验证码表 + 登录失败锁定表（防爆破）
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7f3a9c2d1e45'
down_revision: Union[str, Sequence[str], None] = '201e8719b346'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'verification_codes',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('purpose', sa.String(length=32), nullable=False),
        sa.Column('code_hash', sa.String(length=64), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('attempts', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('ip', sa.String(length=64), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True),
                  server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_index('ix_verification_codes_email', 'verification_codes', ['email'])
    op.create_index('ix_verification_codes_ip', 'verification_codes', ['ip'])

    op.create_table(
        'login_attempts',
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('fail_count', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('locked_until', sa.DateTime(timezone=True), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True),
                  server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('email'),
    )


def downgrade() -> None:
    op.drop_table('login_attempts')
    op.drop_index('ix_verification_codes_ip', table_name='verification_codes')
    op.drop_index('ix_verification_codes_email', table_name='verification_codes')
    op.drop_table('verification_codes')
