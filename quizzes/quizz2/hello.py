from flask import json,jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"
    
@app.route('/users', methods=['POST'])
def new_users():
    data = {
        'id' : 1,
        'name' : 'foo'
    }
    js = json.dumps(data)
    resp = jsonify(data)
    resp.status_code = 200
    return resp
