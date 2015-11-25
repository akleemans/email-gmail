#!/usr/bin/python
# -*- coding: ascii -*-

'''
Sends an email via gmail, plain (send_email) or with attachment (send_email_att).

For sending emails with Gmail, first activate "less secure apps" at
https://www.google.com/settings/security/lesssecureapps

Part of the code from from http://naelshiab.com/tutorial-send-email-python.
'''

import smtplib

def send_email(user, pwd, recipient, subject, message):
    """ Send a simple email with subject and message body. """
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(user, pwd)
    headers = "\r\n".join(["from: " + user, "subject: " + subject, "to: " + recipient, "mime-version: 1.0", "content-type: text/html"])
    content = headers + "\r\n\r\n" + message
    session.sendmail(user, recipient, content)
    session.quit()
    print 'Email succesfully sent.'

def send_email_att(user, pwd, recipient, subject, message, path_to_file):
    """ Send an email with attachment. """
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEBase import MIMEBase
    from email import encoders
     
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    filename = path_to_file.split("/")[-1]
    attachment = open(path_to_file, "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
     
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(user, pwd)
    
    session.sendmail(user, recipient, msg.as_string())
    session.quit()
    print 'Email with attachment succesfully sent.'


# examples
send_email('from-email@gmail.com', 'password', 'to-email@gmail.com', 'subject', 'Example message')
send_email_att('from-email@gmail.com', 'password', 'to-email@gmail.com', 'subject', 'See Attach.', 'D:/projects/example.pdf')

