import smtplib
from email.mime.text import MIMEText

def send_basic_email():
    # SMTP server details for Gmail
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    sender_email = "vlisara1111@gmail.com"
    sender_password = "rodhrfmdzpvdloxa" #password from 2 step verification
    recipient_email = "vinumihewamadduma@gmail.com"

    subject="Stock price alert"
    body= "Hello! This is a mail from your stock moniter."

    # Create MIMEText object
    message = MIMEText(body)
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject']= subject

    # Connect to Gmail SMTP server
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email,sender_password)
        server.send_message(message)
        print("Email sent succesfully")
    except Exception as e:
        print(f"error: {e}")
    finally:
        server.quit()

if __name__=="__main__":
    send_basic_email()
