from flask_json import FlaskJSON, JsonError, json_response, as_json
from flask import request, Flask, jsonify, make_response




app = Flask(__name__)

@app.route('/')
def test():
    return "Hello World"

@app.route('/test', methods=['GET', 'OPTIONS'])
def hello():
    if request.method == 'OPTIONS':
        # Handle the preflight request
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers");
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    elif request.method == 'GET':
        return "{'message': 'This is a Default GET Message.!'}"

@app.route('/test', methods=['POST'])
def get_data():
    status = "True"
    result = {}
    data = request.get_json(force=True)
    req = data['req']
    return {'REQ' : req}

    """
    num1 = data['num1']
    num2 = data['num2']
    res = data['res']
    result = int(num1) + int(num2)
    if(result == int(res)):
        return {'status': 'Valid'}
    else:
       return {'status':'InValid', 'result': result}
    """
