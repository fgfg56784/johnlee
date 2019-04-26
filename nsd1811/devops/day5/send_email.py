#! /usr/local/bin/python3
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from  sys import argv
from getpass import getpass

def message_cont(subject, content, sender, passwd, receivers, url):
    message = MIMEText(content, 'zabbix', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(url)
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_string())

if __name__ == "__main__":
    subject= 'zabbix warning'
    content= argv[1]
    sender='513054325@qq.com'
    passwd='nvtivkwhfcwibjje'
    receivers=['513054325@qq.com']
    url='smtp.qq.com'
    # passwd = getpass('密码: ')

    message_cont(subject, content, sender, passwd, receivers, url)



