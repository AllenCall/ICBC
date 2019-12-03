from flask import Flask,views,render_template,redirect,url_for,request,session,current_app,g,abort
import config
from exts import db
from models import User,Article,Tag
from forms import registForm,loginForm,transferForm
from auth import login_required
from flask_wtf import CSRFProtect
from signals import login_signal
from controllers.restView import rest_bp

app = Flask(__name__)
app.config.from_object(config)
# CSRFProtect(app)
db.init_app(app)
app.register_blueprint(rest_bp)
# api = Api(app)


with app.app_context():
    print(current_app.name)

@app.route('/')
def hello_world():
    # user1 = User(email='310315734@qq.com',userName='llj',passWord=123456)
    # user2 = User(email='***@star-net.cn',userName='allen',passWord=123456)
    # article1 = Article(articleName='红楼梦')
    # article2 = Article(articleName='三国演义')
    # tag1 = Tag(tag='nice')
    # tag2 = Tag(tag='cute')
    # article1.author = user1
    # article2.author = user2
    # print(type(article1.tags))
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.commit()
    # a=1/0
    # abort(500)
    login_signal.send(username = g.username)
    # abort(500)
    return render_template('index.html')

class registView(views.MethodView):
    def get(self):
        return render_template('regist.html')
    def post(self):
        form = registForm(request.form)
        if form.validate():
            email = form.email.data
            userName = form.userName.data
            passWord = form.passWord.data
            balance = form.balance.data
            user = User(email = email,userName = userName,passWord = passWord,balance = balance)
            db.session.add(user)
            db.session.commit()
            return '注册成功！'

class registView(views.MethodView):

    def get(self):
        return render_template('regist.html')

    def post(self):
        form = registForm(request.form)
        if form.validate():

            email = form.email.data
            userCheck = User.query.get(email)
            if userCheck:
                return '该用户已经注册！'
            userName = form.userName.data
            passWord = form.passWord.data
            balance = form.balance.data
            user = User(email = email,userName = userName,passWord = passWord,balance = balance)
            db.session.add(user)
            db.session.commit()
            return '注册成功！'
        else:
            print(form.errors)
            return '注册失败！'

class loginView(views.MethodView):

    def get(self):

        return render_template('login.html')

    def post(self):

        csrf_token = session.get('csrf_token')
        # print("=" * 30)
        # print(csrf_token)
        # print("=" * 30)

        form = loginForm(request.form)
        email = form.email.data
        passWord = form.passWord.data
        user = User.query.filter_by(email=email,passWord=passWord).first()
        # user = User.query.filter(User.email==email, User.passWord==passWord).first()
        if user:
            session['user_email'] = user.email
            return '登录成功！'
        else:
            return '邮箱或密码错误!'

class transferView(views.MethodView):

    decorators = [login_required]

    def get(self):
        return render_template('transfer.html')

    def post(self):
        form = transferForm(request.form)
        email = form.email.data
        balance = form.balance.data
        receiver = User.query.get(email) # 收款人是否存在
        sender_email = session.get('user_email')
        # if sender_email:  # 校验当前是否处于登录状态
        sender = User.query.get(sender_email)
        if receiver:
                # 校验余额
                if sender.balance >= balance:
                    sender.balance -= balance
                    receiver.balance += balance
                    db.session.commit()
                    return '转账成功'
                else:
                    return '余额不足！'
        else:
            return '收款人账号不存在！'
        # else:
        #     return redirect(url_for('login'))

app.add_url_rule('/regist/',view_func = registView.as_view('regist'))
app.add_url_rule('/login/',view_func = loginView.as_view('login'))
app.add_url_rule('/transfer/',view_func = transferView.as_view('transfer'))

with app.test_request_context():
    print(url_for('login'))

@app.route('/virus/')
def virus():
    return render_template('virus.html')

@app.route('/virus_transfer/')
def virus_transfer():
    return render_template('virus_transfer.html')



@app.before_request
def before_request():
    g.username = 'llj'

@app.context_processor
def user():
    return {'username':g.username}

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'),500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
# 位置和关键字参数
# def hh(*args,**kwargs):
#     print('111111111111111111111111111111')
#     print(type(args))
#     print(type(kwargs))
#     print(args[0])
#     print(kwargs['name'])
# hh(6,5,3,name='llj',age=18)
if __name__ == '__main__':
    # api = Api(app)
    app.run(debug=True)



