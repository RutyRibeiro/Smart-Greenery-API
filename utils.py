from datetime import datetime,timezone,timedelta
from validate_email import validate_email
import uuid
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

# Classe para validação de formulários
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
            return({'message':{'title':'Erro',
                'content': str(error)},
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

    def validateForm(self,form,param):
        self.param= param
        self.form = form

        verifyExistance = self._verifyExistance()

        if verifyExistance['status'] == 'erro':
            return verifyExistance
        
        return self._verifyIsEmpty()


# Classe para funções uteis 
class utils():
    # codifica senha no padrão MD5
    def passwordEncode(self, password):
        new_password = hashlib.md5(password.encode())

        return new_password.hexdigest()

    # Gera id unico randomicamente  
    def idGenerator(self):
        newId = str(uuid.uuid1())
        return newId
    
    # verifica se o email informado é valido
    def emailVerify(self, email):
        validate = validate_email(email_address = email, check_regex = True, check_mx = False)
        return validate

    # Captura a data do sistema considerando fuso horario
    def dateCapture(self):
        date = (datetime.now().astimezone(timezone(timedelta(hours=-3)))).strftime('%Y/%m/%d')
        return date

# form={
#     "email":"ruty.pena@gmail.com",
#     # "senha":"senha"
# }
# param = ['email','senha']
# validacao= Validate()

# print(validacao.validateForm(form=form, param=param))








