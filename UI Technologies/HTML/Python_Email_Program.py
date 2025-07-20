import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self, sender_email, sender_password, smtp_server="smtp.mail.yahoo.com", smtp_port=587):
        """Initialize the email sender with Yahoo email settings."""
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    #@staticmethod
    def generate_otp(self, length=6):
        """Generate a random OTP of a given length."""
        otp = ''.join(random.choices(string.digits, k=length))
        return otp

    def send_email(self, otp, recipient_email):
        """Send the OTP to the recipient via email."""
        # Create the email message
        subject = "Your One-Time Password (OTP)"
        body = f"Your OTP is: {otp}"

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Set up the server and send the email
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Secure the connection using TLS
            print(otp, recipient_email)
            server.login(self.sender_email, self.sender_password)  # Log in to the Yahoo account
            print("login success...")
            text = msg.as_string()
            server.sendmail(self.sender_email, recipient_email, text)
            print("Email Sent...")
            server.quit()  # Quit the server after sending the email
            print(f"OTP sent to {recipient_email}")
        except Exception as e:
            print(f"Error sending email: {e}")


# Usage example
if __name__ == "__main__":
    # Replace with your Yahoo email and password (or app password)
    sender_email = "xyz@yahoo.com"
    sender_password = "ppejfvxdgfqvqeor" #"Sayed08@sabeeha"  # Use app password if 2FA is enabled
    # Gmial App Pass: fbxj wjwt ltbu zkvj

    # Create an instance of EmailSender
    email_sender = EmailSender(sender_email, sender_password)

    # Generate an OTP
    otp = email_sender.generate_otp()

    # Define the recipient's email address
    recipient_email = "abc@gmail.com"

    # Send the OTP to the recipient
    email_sender.send_email(otp, recipient_email)
