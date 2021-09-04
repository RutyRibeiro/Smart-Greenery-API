import sys
sys.path.append('../')
from utils import Validate, utils
from ..Handlers.ResponseHandler import ResponseHandler

class User():

    def __init__(self):
        self.id = ''
        self.email =''
        self.password =''
        self.name=''
        self.date=''
        self.responseHandler = ResponseHandler()
    
    def _validateUserLogin(self, user):
        try:
            valida = Validate()
            
            param = ['email','senha']
            validate = valida.validateForm(form = user, param = param)

            if validate['status'] =='erro':
                raise Exception(validate['message']['content'])

            self.email=user['email']
            self.password=user['senha']           

            return validate
        
        except Exception as error:
            return self.responseHandler.error(title='Erro',content=str(error))

    
    def _userExistsAndValidatePassword(self):
        try:
            conn = self._openAndValidateConnection()

            if type(conn) == dict:
                raise Exception (conn['message'])
            
            cursor = conn.cursor()

            cursor.callproc('loginTeste', [self.email,])
                
            for result in cursor.stored_results():
                row = result.fetchall()

            cursor.close()

            self._closeConnection(conn=conn)

            if len(row) == 0:
                    raise Exception('Email ou senha incorreto(s)!')
            
            encode=utils()

            if encode.passwordEncode(password = self.password) != row[0][3]:
                raise Exception('Email ou senha incorreto(s)!')

            self.id = row[0][0]
            self.name = row[0][1]

            return self.responseHandler.success(title='Sucesso',content='Usuário existente no banco de dados')
        
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})
    
    # def getUser(self):
    #     try:
    #         conn = self._openAndValidateConnection()

    #         if type(conn) == dict:
    #             raise Exception (conn['message'])
            
    #         cursor = conn.cursor()


    
    def login(self, user):
        try:
            validate = self._validateUserLogin(user=user)

            if validate['status'] == 'erro':
                raise Exception(validate['message']['content'])
            
            getUser = self._userExistsAndValidatePassword()

            if getUser['status'] == 'erro':
                raise Exception(getUser['message']['content'])
                
            return getUser
            
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})


user1={
        "email":"teste@teste.com",
        "senha":"teste45"
    }
usera=User()

response = usera.login(user=user1)
print(response)


