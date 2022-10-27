from crypt import methods
from ctypes import sizeof
from unicodedata import name
from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#sql配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/Lyric'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#User表相关操作
class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String, primary_key = True)
    age = db.Column(db.Integer)
    score = db.Column(db.String)
    
    def __init__(self, v_name=None, v_age=None, v_score=None):
        self.name = v_name
        self.age = v_age
        self.score = v_score
    def select_all(self):
        return self.query.all()
    def select(self, key):
        if key == 'name':
            return self.query.filter_by(name=self.name)
        elif key == 'age':
            return self.query.filter_by(age=self.age).all()
        elif key == 'score':
            return self.query.filter_by(score=self.score).all()
    def insert(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        

@app.route('/', methods=['GET'])
def index_get():
    user = User('小莫')
    res0 = user.select('name')
    res1 = {'name' : res0[0].name, 'age' : res0[0].age, 'score' : res0[0].score, 'method' : 'this is GET'}
    rsp = make_response(jsonify({'message' : res1}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp
@app.route('/', methods=['POST'])
def index_post():
    user = User('小莫')
    res0 = user.select('name')
    res1 = {'name' : res0[0].name, 'age' : res0[0].age, 'score' : res0[0].score, 'method' : 'this is POST'}
    rsp = make_response(jsonify({'message' : res1}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)