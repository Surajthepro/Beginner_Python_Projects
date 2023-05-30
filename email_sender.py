from email.message import EmailMessage
import ssl
import smtplib

passkey = "" #put passkey
email = "" #put email
subject = "Test Mail"
body = """
This mail is system generated
"""
email_reciever = "" #senders email
em = EmailMessage()
em['subject'] = subject
em['From'] = email
em['To'] = email_reciever
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email,passkey)
    smtp.sendmail(email,email_reciever,em.as_string())

