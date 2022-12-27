from crypt import methods
from ctypes import sizeof
from flask import Flask, request, make_response, jsonify, session, Response
from flask.sessions import SecureCookieSessionInterface
from flask_cors import CORS
import json
import os
from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
#axios通信设置
app.config['SECRET_KEY'] = os.urandom(24)
# CORS(app)#"supports_credentials": True, 
CORS(app, resources={r"/*": {"origins":'*', "supports_credentials": True}})#"supports_credentials": True, 
user_id_set = 0
session_backups = []

#sql配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/HDACP'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#User表相关操作
class MD(db.Model):
    __tablename__ = 'md'
    id = db.Column(db.String, primary_key = True)
    title = db.Column(db.String)
    text = db.Column(db.String)


@app.route('/', methods=['POST', 'GET'])
def select_all():
    getData = request.get_data().decode("utf-8")
    sql_res = MD.query.all()
    res = []
    for r in sql_res:
        tmp_dict = {"id" : r.id, "title" : r.title};
        res.append(tmp_dict)
    print(f"select_all : {res}")
    rsp = None
    if res != []:
        rsp = make_response(res, 200)
    else:
        rsp = make_response(jsonify({'message' : '无此用户'}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    rsp.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return rsp

@app.route('/select_one', methods=['POST', 'GET'])
def select_one():
    getData = request.get_data().decode("utf-8")
    getData = json.loads(getData)
    print(f"select_one : {getData}")
    sql_res = MD.query.filter(MD.id == getData['id']).first()
    res = ""
    res = sql_res.text
    print(f"select_one : {res}")
    rsp = None
    if res != []:
        rsp = make_response(res, 200)
    else:
        rsp = make_response(jsonify({'message' : '无此用户'}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    rsp.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return rsp

@app.route('/addnew', methods=['POST', 'GET'])
def addnew():
    getData = request.get_data().decode("utf-8")
    getData = json.loads(getData)
    print(f"addnew : {getData}")
    sql_res = MD.query.all()
    nextid = int(sql_res[-1].id) + 1
    print(F"addnew : nextid = {nextid}")
    newmd = MD(id=nextid, title=getData['title'], text=getData['text'])
    db.session.add(newmd)
    db.session.commit()
    res = "1"
    rsp = None
    if res != []:
        rsp = make_response(res, 200)
    else:
        rsp = make_response(jsonify({'message' : '无此用户'}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    rsp.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return rsp

@app.route('/fixone', methods=['POST', 'GET'])
def fixone():
    getData = request.get_data().decode("utf-8")
    getData = json.loads(getData)
    print(f"fixone : {getData}")
    sql_res = MD.query.filter(MD.id == getData['id']).update({MD.text : getData['text']})
    # db.session.add(newmd)
    db.session.commit()
    res = "1"
    rsp = None
    if res != []:
        rsp = make_response(res, 200)
    else:
        rsp = make_response(jsonify({'message' : '无此用户'}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    rsp.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return rsp

@app.route('/delete', methods=['POST', 'GET'])
def deletemd():
    getData = request.get_data().decode("utf-8")
    getData = json.loads(getData)
    print(f"deletemd : {getData}")
    MD.query.filter(MD.id == getData['id']).delete()
    db.session.commit()
    rsp = make_response(jsonify({'message' : '已删除'}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    rsp.headers['Access-Control-Allow-Credentials'] = 'true'
    
    return rsp

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)