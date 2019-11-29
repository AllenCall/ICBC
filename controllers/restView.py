from flask_restful import Api,Resource,reqparse,inputs,marshal_with,fields
from models import User
from flask import Blueprint
rest_bp = Blueprint('rest',__name__,url_prefix='/rest')
api  = Api()
class restView(Resource):

    resource_fields = {
        'userName':fields.String
    }

    @marshal_with(resource_fields)
    def post(self,username = None):
        parse = reqparse.RequestParser()
        parse.add_argument('username', type=str, help='请输入用户名！')
        parse.add_argument('age', type=int, help='请输入年龄！')
        parse.add_argument('birthday',type=inputs.date,help='时间输入不正确！',required = True)
        args = parse.parse_args()
        print(args)
        user = User.query.filter_by(userName=username).first()
        return user
    def get(self):
        return {'test': 'get'}
api.add_resource(restView,'/rest/<username>',endpoint = 'rest')
