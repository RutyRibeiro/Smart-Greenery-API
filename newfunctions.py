from mysql.connector import errorcode
import os
from dotenv import load_dotenv
import connection
import utils

class User():
    
    def __init__(self):
        self.email =''
        self.password =''
        self.name=''
        self.date=''
        self.validacao = utils.Validate()
    def _validateUser(self, user):
        try:
            self.validacao.form={
                "email":user['email'],
                "senha":user['senha']
                } 
            self.validacao.param = ['email','senha']
            
            validate = self.validacao.validadeForm()

            if 'erro' in validate:
                raise Exception(validate)

            self.email=user['email']
            self.password=user['senha']
        
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': error},
                'status':'erro'})
            
        

    # def login(self):
        
    #     result = self._validateUser

    #     if result

    #     if 'erro' in result:
    #         return result

    user={
        "email":"ruty.pena@gmail.com",
        "senha":"senha"
    }

    




