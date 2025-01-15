import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, message_body):
    sender_email = "your-email@gmail.com"
    sender_password = "your-password"

    msg = MIMEText(message_body)
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
