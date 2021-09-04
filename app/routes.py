from app import app
from flask_cors import CORS, cross_origin
from flask import request, jsonify
from .Handlers import ResponseHandler

responseHandler = ResponseHandler.ResponseHandler()

@app.route('/')

@app.route('/index')
def index():
    return "Server ok"

@app.route('/user/get', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def getUser():
    userEmail = request.headers.get('user-email') or False
    if(userEmail == False):
        return responseHandler.error('Erro', 'Não foram enviadas as informações necessárias nos headers'), 400
    
    return  userEmail

@app.route('/user/register/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def createUser():
    return 'Usuário criado', 201

@app.route('/user/login/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def logUser():
    return 'O usuário esta logado',300


@app.route('/user/modify/', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyUser():
    return 'O usuário foi alterado',300

@app.route('/user/retrieve/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def retrieveUser():
    return 'Um email foi enviado para voc',300

@app.route('/plant/register', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def registerPlant():
    return 'A planta foi criada',201

@app.route('/plant/delete', methods=['DELETE'])
@cross_origin(origin='*',headers=['Content-Type'])
def deletePlant():
    return 'A planta foi deletada',200

@app.route('/plant/modify', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyPlant():
    return 'Planta alterada',200

@app.route('/greenery/modify', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyGreenery():
    return 'O nome da estufa foi alterado',200




    

