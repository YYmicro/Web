from crypt import methods
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def func():
    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    print(data)
    rsp = make_response(jsonify({'name' : data["name"], 'sex' : "男" if data["sex"]=="1" else "女"}), 200)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    print(rsp.data)
    return rsp
if __name__ == '__main__':
    app.run('127.0.0.1', '5000', True)