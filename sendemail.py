#!/usr/bin/env python
# encoding: utf-8
"""
python_3_email_with_attachment.py
Created by Robert Dempsey on 12/6/14.
Copyright (c) 2014 Robert Dempsey. Use at your own peril.
This script works with Python 3.x
NOTE: replace values in ALL CAPS with your own values
"""
import sys
import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import datetime
from email.mime.text import MIMEText


COMMASPACE = ', '
def mainSendMail(senderUser, HisSubject, hismessage):
    text = hismessage
    sender = '' #SenderUser email ID
    gmail_password = '' #Password
    if senderUser and senderUser !="":
        recipients.append(senderUser)
    else:
        return
    # Create the enclosing (outer) message
    outer = MIMEMultipart()
    outer['Subject'] = HisSubject
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # List of attachments
    attachments = ['']

    # Add the attachments to the message
    for file in attachments:
        try:
            outer.attach(MIMEText(text, 'plain'))
            # with open(file, 'rb') as fp:
                # msg = MIMEBase('application', "octet-stream")
                # msg.set_payload(fp.read())
            # encoders.encode_base64(msg)
            # msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            # outer.attach(msg)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    