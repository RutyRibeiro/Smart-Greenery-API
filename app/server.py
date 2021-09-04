from flask import Flask, request
from flask_cors import CORS, cross_origin
import cv2
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("LOCAL"))
if os.getenv("LOCAL") == 'dev':
    from functions import login, register, retrieve, greenregister, elementregister
    port = '4000'

else:
    from backend.functions import login, register, retrieve, greenregister, elementregister
    port = int(os.environ.get('PORT', 33507))

app = Flask('Greenery')
cors = CORS(app, resources={r"/": {"origins": "*"}})

@app.route('/login', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def tologin():
    user = request.get_json()
    response =  login(user)
    return response

@app.route('/register', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def toregister():
    user = request.get_json()
    response =  register(user)
    return response

@app.route('/retrieve', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def toretrieve():
    user = request.get_json()
    response = retrieve(user)
    return response

@app.route('/greenregister', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def green_register():
    green = request.get_json()
    response = greenregister(green)
    return (response)

@app.route('/elementregister', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def element_register():
    element = request.get_json()
    response = elementregister(element)
    return (response)

@app.route('/', methods=['DELETE'])
def delete():

    return ('DELETE')

app.run(port=port, host='0.0.0.0')



