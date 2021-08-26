from datetime import datetime,timezone,timedelta
from validate_email import validate_email
import uuid
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

class Validate():
    def __init__(self):
        self.param = []
        self.form = {}
    
    def _verifyExistance(self):
        try:
            for field in self.param:
                if field not in self.form:
                    raise Exception(f"O campo {field} é inexistente")
            return({
                    "status":"ok",
                    "message":"Campos validados"
                    })
        except Exception as error:
            # verificar porque não está devolvendo toda mensagem de erro em 'content'
            erro = str(error)
            return({'message':{'title':'Erro',
                'content': erro},
                'status':'erro'})

    
    def _verifyIsEmpty(self):
        try:
            for field in self.param:
                if self.form[field] is None or self.form[field] =='':
                    raise Exception(f"O campo {field} está vazio")
            return({
                    "status":"ok",
                    "message":"Campos validados"
                    })            
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

    def validadeForm(self):
        verifyExistance = self._verifyExistance()
        print(verifyExistance)
        if 'erro' in verifyExistance:
            return verifyExistance
        
        return self._verifyIsEmpty()

validacao = Validate()
validacao.form={
    "email":"ruty.pena@gmail.com",
    # "senha":"senha"
}
validacao.param = ['email','senha']

print(validacao.validadeForm())





