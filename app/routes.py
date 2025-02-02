import sys
sys.path.append('../')
from app import app
from flask_cors import CORS, cross_origin
from flask import request
from .Handlers.ResponseHandler import ResponseHandler
from .Controllers.UserController import User
from .Controllers.GreenerysController import Greenery
from .Controllers.ElementController import Element
from .Controllers.PlantController import Plant

responseHandler = ResponseHandler()
user = User()
greenery= Greenery()
element = Element()
plant = Plant()

@app.route('/')
@app.route('/index')
def index():
    return "Server ok"

@app.route('/user/register/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def createUser():
    response = user.register(request.get_json())
    return response

@app.route('/user/login/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def logUser():
    response = user.login(request.get_json())
    return response

@app.route('/user/modify/', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyUser():
    response = user.modify(request.get_json())
    return response

@app.route('/user/retrieve/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def retrieveUser():
    email = request.headers.get('email') or False 
    
    if(email == False):
        return responseHandler.error(content='Não foram enviadas as informações de email necessárias nos headers'), 400
    
    response = user.retrieve(user=email)
    return response

@app.route('/user/confirmretrieve/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def confirmRetrieve():
    response = user.confirmRetrieve(user=request.get_json())
    return response

@app.route('/plant/register/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def registerPlant():
    response = plant.createPlant(plant=request.get_json())
    return response

@app.route('/plant/delete/', methods=['DELETE'])
@cross_origin(origin='*',headers=['Content-Type'])
def deletePlant():
    plantId = request.headers.get('id-planta') or False 
    if(plantId == False):
        return responseHandler.error(content = 'Não foram enviadas as informações de planta necessárias nos headers'), 400
    
    response = plant.deletePlant(idPlant=plantId) 
    
    return  response

@app.route('/plant/modify/', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyPlant():
    response = plant.modifyPlant(plant = request.get_json())
    return response

@app.route('/greenery/get/', methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def getGreenery():
    userId = request.headers.get('user-id') or False 
    if(userId == False):
        return responseHandler.error(content = 'Não foram enviadas as informações de estufa necessárias nos headers'), 400
   
    return  greenery.formatGreenerys(userId=userId)

@app.route('/greenery/modify/', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyGreenery():
    response = greenery.modifyGreenery(request.get_json())
    return response

@app.route('/element/modify/', methods=['PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def modifyElement():
    response = element.modifyElement(request.get_json())
    return response




    

