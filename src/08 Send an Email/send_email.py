''' Send an email

Notice: Google requires usage of an “App Password“. This is a 16-digit passcode that 
is generated in Google account. It allows less secure apps or devices that don’t support
2-step verification to sign in to Gmail Account. 

Output: 
    Message to recipient_1@gmail.com sent
'''

import smtplib
# Email module provides classes for constructing and parsing email messages (To, From, Subject ...)
# and encoding and decoding emails with the MIME (Multipurpose Internet Mail Extensions) standard.
from email.mime.text import MIMEText

def send_email(recipients, subject, body):
    ''' Send an email using gmail smtp server. '''
    sender = "sender@gmail.com"
    password = "Google account App password"
    # Create the email message using the MIMEText object, and set the desired values.
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print(f"Message to { msg['To'] } sent")


if __name__ == '__main__':
    # Add one or more recipients
    recipients = ["recipient_1@gmail.com"]
    subject = "Christmas coding challenge 2023"
    body = "This email is part of the Christmas coding challenge 2023."
    send_email(recipients, subject, body)
