from flask import Flask, request
from bd_functions import login

app = Flask('Greenery')

@app.route('/login', methods=['POST'])
def post():
    user = request.get_json()
    response =  login(user)
    return response

@app.route('/', methods=['GET'])
def get():

    return ('GET')


@app.route('/', methods=['PUT'])
def put():

    return ('PUT')

@app.route('/', methods=['PATCH'])
def patch():

    return ('PATCH')

@app.route('/', methods=['DELETE'])
def delete():

    return ('DELETE')

app.run(port='4000')



