import logging
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from config import GMAIL_USER, GMAIL_PASSWORD

# Send an email to the designated email with the passed subject and html body
def send_email(email, subject, html):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = GMAIL_USER
    msg['To'] = email
    msg.attach(MIMEText(html, 'html'))

    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, email, email_text)
        server.close()

        # logging.info('Sent Application Confirmation Email to %s', email)
        print 'It worked!'
    except:  
        # logging.info('FAILED Sending Application Confirmation to %s', email)
        print 'Something went wrong...'


