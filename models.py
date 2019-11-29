from exts import db
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    email = db.Column(db.String(50))
    userName = db.Column(db.String(50))
    passWord = db.Column(db.String(10))
    balance = db.Column(db.Float,default=0)

article_tag_table = db.Table(
    'article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    articleName = db.Column(db.String(50))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    author = db.relationship('User',backref = 'articles')
    tags = db.relationship('Tag',secondary = article_tag_table,backref = 'articles')

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    tag = db.Column(db.String(12))


if __name__ == '__main__':
    pass