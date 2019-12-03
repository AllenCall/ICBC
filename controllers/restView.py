from flask_restful import Api,Resource,reqparse,inputs,marshal_with,fields
from models import User
from flask import Blueprint, make_response, render_template

rest_bp = Blueprint('rest',__name__,url_prefix='/user_info')
api  = Api(rest_bp)

@api.representation('text/html')
def output_html(data,code,headers):
    resp = make_response(data)
    return resp

class restView(Resource):

    resource_fields = {
        'username':fields.String(attribute='userName'),
        'articles':fields.List(fields.Nested({
            'articleName':fields.String
        }))
    }

    @marshal_with(resource_fields)
    def post(self,username = None):
        parse = reqparse.RequestParser()
        parse.add_argument('username', type=str, help='请输入用户名！')
        parse.add_argument('age', type=int, help='请输入年龄！')
        parse.add_argument('birthday',type=inputs.date,help='时间输入不正确！',required = True)
        print('1111111111111111111111')
        args = parse.parse_args()
        user = User.query.filter_by(userName=args['username']).first()
        return user
    def get(self):
        return render_template('404.html')
api.add_resource(restView,'',endpoint = 'user_info')
