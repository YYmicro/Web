from crypt import methods
from ctypes import sizeof
from flask import Flask, request, make_response, jsonify, session, Response
from flask.sessions import SecureCookieSessionInterface
from flask_cors import CORS
import json
import os
from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#axios通信设置
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, resources={r"/*": {"origins":'*', "supports_credentials": True}})#"supports_credentials": True, 
user_id_set = 0
session_backups = []

#sql配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/HDACP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#User表相关操作
class User(db.Model):
    __tablename__ = 'user'
    userid = db.Column(db.String, primary_key = True)
    name = db.Column(db.String)
    level = db.Column(db.Integer)
    email = db.Column(db.String)
    
    def __init__(self, v_userid = None, v_name = None, v_level = None, v_email = None):
        self.userid = v_userid
        self.password = v_password
        self.name = v_name
        self.email = v_email

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


@app.route('/', methods=['POST', 'GET'])
def func():
    userid = request.get_data().decode("utf-8")
    user = User()
    res0 = user.select('userid', userid)
    rsp = None
    if res0 != []:
        rsp = make_response(jsonify({'message' : res0[0].name}), 200)
    else:
        rsp = make_response(jsonify({'message' : '无此用户'}), 200)
    print(rsp)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)