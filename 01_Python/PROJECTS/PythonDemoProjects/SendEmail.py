# Write a script to automate sending daily email reports in Python, and walk me through how I would set it up.

import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from datetime import datetime 


def send_email():
    # Email credentials 
    sender_email = "sayedmahfuze@yahoo.com"
    sender_password = "Sayed08@sabeeha"
    app_password = "edaiuldbsobpgpkn"
    receiver_email = "x2xcyrus@gmail.com"


    # Create the email content 
    subject = f"Daily Report - {datetime.now().strftime('%Y-%m-%d')}"
    body = "This is your daily report from Yahoo App. \n\nBest Regards, \nYour Automated SYstem"


    # Setup the MIME 
    msg = MIMEMultipart()
    msg['From'] = sender_email 
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body to the email 
    msg.attach(MIMEText(body, 'plain'))

    # Setup the server and send the email 
    try:
        #server = smtplib.SMTP('smtp.gmail.com', 587)  # Port: SSL: 465, TLS: 587
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()



#  import schedule 
# import time 

# def job():
#    send_email()


# schedule.every().day.at("08:00").do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

if __name__ == "__main__":
    send_email()




