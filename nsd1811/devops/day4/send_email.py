from email.mime.text import MIMEText
from email.header import Header
import smtplib
from getpass import getpass

def send_mail(msg, subject, sender, receivers, host, passwd):
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    smtp = smtplib.SMTP()
    smtp.connect(host)
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == "__main__":
    msg = 'python smtplib 邮件测试\r\n'
    subject = 'py mail test'
    sender = '513054325@qq.com'
    receivers = ['']
    host = 'smtp.qq.com'
    passwd = getpass('密码: ')

    send_mail(msg, subject, sender, receivers, host, passwd)
