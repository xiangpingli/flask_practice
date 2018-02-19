from flask import Flask 
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config.update(
    DEBUG = True,
    MAIL_SERVER='smtp.aliyun.com',
    MAIL_PORT=25,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    #MAIL_USERNAME = 'lixiangping@aliyun.com',
    #MAIL_PASSWORD = 'lxp19860112lxp',
    MAIL_USERNAME='627607086@qq.com',
    MAIL_PASSWORD='sctixyxcmklxbega'
)

mail = Mail(app)

def mail_send():
    #msg = Message("Hi!This is a test ",sender='lixiangping@aliyun.com', recipients=['lixiangping@aliyun.com'])
    msg = Message("Hi!This is a test ",sender='627607086@qq.com', recipients=['627607086@qq.com'])
    msg.body = "This is a first email"
    msg.html = '<b>HTML</b>'
    with app.app_context():
        mail.send(msg)
    
    print "Mail sent"

if __name__ == "__main__":
    mail_send()
