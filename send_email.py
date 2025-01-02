import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

# Load env vars
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read env vars
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")

def send_email(subj, recv, name, due_date, invoice_no, amt):
    # Create base text msg
    msg = EmailMessage()
    msg["Subject"] = subj
    msg["From"] = formataddr(("Coding is Fun", sender_email))
    msg["To"] = recv
    msg.set_content(
        f"Hi {name},\n"
        f"I hope you are well.\n"
        f"I just wanted to drop you a quick note to remind you that {amt} USD in respect of our "
        f"invoice {invoice_no} is due for payment on {due_date}.\n"
        "I would be really grateful if you could confirm that everything is on track for payment.\n"
        "Best regards,\nSriya"
    )
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password_email)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
