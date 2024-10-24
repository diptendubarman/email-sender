# tasks.py

from app.celery_worker import celery
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

smtp_host = os.getenv("SMTP_HOST", "sandbox.smtp.mailtrap.io")
smtp_port = os.getenv("SMTP_POST", "2525")
smtp_username = os.getenv("SMTP_USERNAME", "xxxxxxxxxxxxxx")
smtp_password = os.getenv("SMTP_PASSWORD", "xxxxxxxxxxxxxx")

@celery.task(name="send_email_task")
def send_email_task(recipient, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = "Test Example <no-reply@example.com>"
        msg['To'] = recipient
        msg['Subject'] = subject
        # Attach plain text part
        part1 = MIMEText(body, 'plain')

        # Attach both parts to the message. Plain text first, then HTML.
        msg.attach(part1)
        
        # Use your SMTP server here
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail("Test Example <no-reply@example.com>", recipient, msg.as_string())

    except Exception as e:
        return str(e)
    return f"Email sent to {recipient}"
