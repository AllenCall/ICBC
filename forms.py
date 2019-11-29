from wtforms import Form,StringField,FloatField
from wtforms.validators import *

class registForm(Form):
    email = StringField(validators=[email()])
    userName = StringField(validators=[length(min=3,max=6,message='用户名长度3-6位')])
    passWord = StringField(validators=[length(min=6,max=10,message='密码长度6-10位')])
    passWordRepeat = StringField(validators=[length(min=6,max=10,message='密码长度6-10位'),EqualTo('passWord',message='两次密码不一致!')])
    balance = FloatField(validators=[input_required()])

class loginForm(Form):
    email = StringField(validators=[email()])
    passWord = StringField(validators=[length(min=6,max=10,message='密码长度6-10位')])

class transferForm(Form):
    email = StringField(validators=[email()])
    balance = FloatField(validators=[input_required()])