from exts import db
class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String(50),primary_key=True)
    userName = db.Column(db.String(50))
    passWord = db.Column(db.String(10))
    balance = db.Column(db.Float,default=0)


