from crypt import methods
from ctypes import sizeof
from unicodedata import name
from flask import Flask, make_response, jsonify, request, request_started
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#sql配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/Lyric'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#User表相关操作
class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.String, primary_key = True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    sex = db.Column(db.String)
    age = db.Column(db.Integer)
    isadmin = db.Column(db.Integer)
    
    def __init__(self, v_userid = None, v_password = None, v_name = None, v_sex = None, v_age = None, v_isadmin = None):
        self.userid = v_userid
        self.password = v_password
        self.name = v_name
        self.sex = v_sex
        self.age = v_age
        self.isadmin = v_isadmin
    def select_all(self):
        return self.query.all()
    def select(self, key, value=None):
        if value == None:
            if key == 'userid':
                return self.query.filter_by(userid=self.userid).all()
        else:
            if key == 'userid':
                return self.query.filter_by(userid=value).all()
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

# @app.route('/', methods=['GET'])
# def index_get():
#     user = User('小莫')
#     res0 = user.select('name')
#     res1 = {'name' : res0[0].name, 'age' : res0[0].age, 'score' : res0[0].score, 'method' : 'this is GET'}
#     rsp = make_response(jsonify({'message' : res1}), 200)
#     rsp.headers['Access-Control-Allow-Origin'] = '*'
#     return rsp
@app.route('/', methods=['POST'])
def index_post():
    userid = request.get_data().decode("utf-8")
    user = User()
    res0 = user.select('userid', userid)
    rsp = None
    if res0 != []:
        rsp = make_response(jsonify({'message' : res0[0].name}), 200)
    else:
        rsp = make_response(jsonify({'message' : '无此用户'}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)