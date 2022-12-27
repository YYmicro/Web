from crypt import methods
from ctypes import sizeof
from unicodedata import name
from flask import Flask, make_response, jsonify, request, request_started
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

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
    num = request.get_data().decode("utf-8")
    rsp = None
    if num == '' or num.isdigit()==False or int(num) > 9 or int(num) < 1:
        rsp = make_response(jsonify({'message' : 'error'}), 200)
    elif num.isdigit():
        res = []
        num = int(num)
        for i in range(1, num+1):
            tmp = ''
            for j in range(1, i+1):
                tmp += str(j) + '*' + str(i) + '=' + str(i*j) + '\t'
            res.append(tmp)
        rsp = make_response(jsonify({'message' : res}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp

if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)