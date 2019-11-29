from blinker import Namespace
from flask import request,template_rendered,got_request_exception
from datetime import datetime
# 信号三步曲
#1、创建信号
login = Namespace()
login_signal = login.signal('login')

#2、监听信号
def login_loggin(sender,username):
    now = datetime.now()
    ip = request.remote_addr
    login_log = 'username:{username},ip:{ip},time:{now}'.format(username = username,ip=ip,now=now)
    with open('login_log.txt','a') as fp:
        fp.write(login_log+'\n')
login_signal.connect(login_loggin)

def template_render(sender,template,context):
    print(sender)
    print('********************')
    print(template)
    print('*****************')
    print(context)
template_rendered.connect(template_render)

def request_exception_log(sender,exception):
    print(exception)
got_request_exception.connect(request_exception_log)