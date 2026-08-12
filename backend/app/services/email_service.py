"""
邮件发送服务（QQ 邮箱 SMTP）

SMTP 配置来自环境变量（见 config.py）。
SMTP 为同步阻塞操作，通过 asyncio.to_thread 放到线程池执行，避免阻塞事件循环。
"""

import asyncio
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from app.core.config import settings


def _send_sync(to: str, subject: str, html: str) -> None:
    msg = MIMEText(html, "html", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = f"{settings.SMTP_FROM_NAME} <{settings.SMTP_USER}>"
    msg["To"] = to

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT, timeout=15) as smtp:
        smtp.login(settings.SMTP_USER, settings.SMTP_PASS)
        smtp.sendmail(settings.SMTP_USER, [to], msg.as_string())


async def send_email(to: str, subject: str, html: str) -> None:
    await asyncio.to_thread(_send_sync, to, subject, html)


def build_code_email(app_name: str, code: str, minutes: int) -> tuple[str, str]:
    """构造验证码邮件，返回 (subject, html)"""
    subject = f"【{app_name}】邮箱验证码"
    html = f"""
    <div style="max-width:480px;margin:0 auto;font-family:-apple-system,'Segoe UI',sans-serif;
                border:1px solid #eee;border-radius:12px;padding:32px;">
      <h2 style="margin:0 0 16px;color:#c026d3;">{app_name}</h2>
      <p style="color:#333;font-size:15px;">你正在注册 {app_name} 账号，验证码为：</p>
      <div style="font-size:32px;font-weight:700;letter-spacing:8px;color:#c026d3;
                  background:#fdf4ff;border-radius:8px;padding:16px;text-align:center;
                  margin:20px 0;">{code}</div>
      <p style="color:#666;font-size:13px;">验证码 {minutes} 分钟内有效，请勿泄露给他人。</p>
      <p style="color:#999;font-size:12px;margin-top:24px;">
        如非本人操作，请忽略此邮件。
      </p>
    </div>
    """
    return subject, html
