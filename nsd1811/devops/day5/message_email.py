#!/usr/local/bin/python3
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys

def message_frame(user):
    message = MIMEText('py test content\r\n', 'root', 'utf8')
    message['From'] = Header('root', 'utf8')
    message['To'] = Header(user, 'utf8')
    message['Subject'] = Header('python测试', 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect('127.0.0.1')
    smtp.sendmail('root', user, message.as_string())
    smtp.close()

if __name__ == "__main__":
    user = sys.argv[1]
    message_frame(user)