from crypt import methods
from ctypes import sizeof
from flask import Flask, request, make_response, jsonify, session, Response
from flask.sessions import SecureCookieSessionInterface
from flask_cors import CORS
import json
import os
from datetime import date, datetime

from sqlalchemy import null


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app, resources={r"/*": {"origins":'*', "supports_credentials": True}})#"supports_credentials": True, 
user_id_set = 0
session_backups = []


@app.route('/', methods=['POST', 'GET'])
def func():
    #获取上传数据
    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    print(f'用户post消息rqt = {request.get_data()}')
    #获取user_id,设置session记录
    user_id = request.cookies.get("id")
    print(f'user_id = {user_id}')
    flag = -1
    global session_backups
    session["user"] = session_backups
    print(session["user"])
    for idx, user in enumerate(session["user"]):
        if user_id != None and user["id"] == eval(user_id):
            flag = idx
            break
    if flag == -1:
        print(f'未匹配到user,注册新信息')
        global user_id_set
        dict_tmp = {"id":user_id_set, "firstTime":str(datetime.now()), "lastTime":str(datetime.now()), "times":0}
        user_id_set += 1
        session["user"].append(dict_tmp)
    else:
        print(f'已匹配到user,idx = {idx}')
        session["user"][flag]["lasTime"] = str(datetime.now())
        session["user"][flag]["times"] += 1
    print(f'服务器更新userid会话ses = {session["user"][flag]}')
    #更新cookies
    rsp = make_response(jsonify(session["user"][flag]))
    rsp.status = 200
    for c in session["user"][flag]:
        print(f'设置cookies中 {c}-{str(session["user"][flag][c])}')
        rsp.set_cookie(c, value=str(session["user"][flag][c]), path='/',httponly=False, domain='127.0.0.1', samesite='None', secure='true')
    print(f'(no error)服务器传回消息rsp = {rsp.data}')
    session_backups = session["user"]
    return rsp
if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)