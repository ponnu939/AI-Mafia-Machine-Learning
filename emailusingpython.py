import smtplib
import getpass
from email.mime.text import MIMEText

def send_email():
    senders_address="anupama10092001@gmail.com"
    password=getpass.getpass()
    print(password)
    subject='Learn.Inspire.Grow'
    message=''' Hey hope you are doing fine
                this is my first time using python to send email
                Thanking you
                Anupama
                '''

    # server initialization
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(senders_address,password)
    recipients="anupama10092001@gmail.com"
    # draft message in body
    msg=MIMEText(message)
    msg["From"]=senders_address
    msg["To"]="anupama10092001@gmail.com"
    msg["Subject"]=subject
    server.sendmail(senders_address,recipients,msg.as_string())
send_email()
