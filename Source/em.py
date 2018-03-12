import db
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import random
import smtplib
_mail='mas.cse.nitk@gmail.com'

def sendemail_verify(toAddr):
    msg = MIMEMultipart()
    msg['Subject'] = ' Multi-Accounting Software'
    msg['From'] = _mail
    msg['To'] = toAddr
    number=random.randint(100000,999999)
    msg.attach(MIMEText('Your Verification Code is:  ' + str(number)))
    #fp = open(_file,'rb')
    #att = MIMEApplication(fp.read())
    #fp.close()
    #att.add_header('Content-Disposition','attachment',filename = _file)
    #msg.attach(att)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        #server.starttls() #starts ttls  # sends hello
        #server.ehlo()
        server.login(_mail,"mascsenitk")  # FInd a way to store the password in a more secure way
        server.sendmail(_mail,toAddr,msg.as_string())
        server.close()
        return 1,number
    except:
        return 0,number
