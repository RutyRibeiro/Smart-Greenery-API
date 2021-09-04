import sys
sys.path.append('../')
from dns.resolver import query
from app.utils.validate import Validate
from app.utils.utils import utils
from app.Handlers.ResponseHandler import ResponseHandler
from app.Handlers.QueryHandler import QueryHandler


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
            queryHandler = QueryHandler()

            queryResult = queryHandler.queryExec(operationType='select',variables=[self.email],proc='loginTeste')

            if type(queryResult) == dict:
                return queryResult

            if len(queryResult) == 0:
                    raise Exception('Credenciais inválidas!')
            
            encode=utils()

            if encode.passwordEncode(password = self.password) != queryResult[0][3]:
                raise Exception('Credenciais inválidas!')

            self.id = queryResult[0][0]
            self.name = queryResult[0][1]

            return self.responseHandler.success(title='Sucesso',content='Usuário existente no banco de dados')
        
        except Exception as error:
            return self.responseHandler.error(title='erro',content=str(error))

    
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
                return validate
            
            getUser = self._userExistsAndValidatePassword()

            if getUser['status'] == 'erro':
                return getUser
                
            return getUser
            
        except Exception as error:
            return self.responseHandler.error(title='erro',content=str(error))



user1={
        "email":"teste@teste.com",
        "senha":"teste45"
    }
usera=User()

response = usera.login(user=user1)
print(response)


