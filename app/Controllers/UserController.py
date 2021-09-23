from logging import exception


if __name__ == 'app.Controllers.UserController':
    from ..Controllers.GreenerysController import Greenery
    from ..Handlers.ResponseHandler import ResponseHandler
    from ..Handlers.QueryHandler import QueryHandler
    from ..utilities.sendEmail import SendEmail
    from ..utilities.validate import Validate
    from ..utilities.utils import utils
else:
    import sys
    sys.path.append('..')
    from utilities.utils import utils
    from utilities.validate import Validate
    from utilities.sendEmail import SendEmail
    from Handlers.QueryHandler import QueryHandler
    from Handlers.ResponseHandler import ResponseHandler
    from Controllers.GreenerysController import Greenery

responseHandler = ResponseHandler()
Utils = utils()

class User():
    def __init__(self):
        self.id = ''
        self.email =''
        self.password =''
        self.name=''
        self.date=''
        self.token=''
    
    def _validateUserLogin(self, user):
        try:
            valida = Validate()
            
            param = ['email','senha']
            validateUserLogin = valida.validateForm(form = user, param = param)
            if validateUserLogin['status'] =='erro':
                raise Exception(validateUserLogin['mensagem']['conteudo'])

            self.email=user['email']
            self.password=user['senha']           

            return validateUserLogin
        
        except Exception as error:
            return responseHandler.error(title='Erro',content=str(error))
    
    def _userExistsAndValidatePassword(self):
        try:
            queryHandler = QueryHandler()

            queryResult = queryHandler.queryExec(operationType='select',variables=[self.email],proc='userLogin')

            if type(queryResult) == dict:
                return queryResult

            if len(queryResult) == 0:
                    raise Exception('Credenciais inválidas!')

            if Utils.passwordEncode(password = self.password) != queryResult[0][3]:
                raise Exception('Credenciais inválidas!')

            self.id = queryResult[0][0]
            self.name = queryResult[0][1]

            return responseHandler.success(title='Sucesso',content='Usuário existente no banco de dados')
        
        except Exception as error:
            return responseHandler.error(title='erro',content=str(error))

    def _formatUser(self):
        try:
            user = {'id': self.id,
            'nome': self.name,
            'email': self.email,
            }
            return responseHandler.success(content = user)
        except:
            return responseHandler.error(content='Erro no servidor!')

    def _validateUserRegister(self, user):
        try:
            valida = Validate()
            
            param = ['email','senha','nome']
            validateUserLogin = valida.validateForm(form = user, param = param)
            if validateUserLogin['status'] =='erro':
                raise Exception(validateUserLogin['mensagem']['conteudo'])

            self.email=user['email']
            self.password=user['senha']           
            self.name=user['nome']           

            return validateUserLogin
        
        except Exception as error:
             return responseHandler.error(title='Erro',content=str(error))

    def login(self, user):
        try:
            validateUserLogin = self._validateUserLogin(user=user)

            if validateUserLogin['status'] == 'erro':
                return validateUserLogin
            
            userExists = self._userExistsAndValidatePassword()

            if userExists['status'] == 'erro':
                return userExists
    
            return self._formatUser()
            
        except Exception as error:
            return responseHandler.error(title='erro',content=str(error))
    
    def register(self, user):
        try:   
            validateRegister = self._validateUserRegister(user=user)

            if validateRegister['status'] == 'erro':
                raise Exception (validateRegister['mensagem']['conteudo'])

            self.id = Utils.idGenerator()
            self.name = user['nome']
            self.password = Utils.passwordEncode(user['senha'])
            self.date = Utils.dateCapture()
            # foto = user['photo']
            self.email = user['email']

            queryHandler = QueryHandler()

            queryResult = queryHandler.queryExec(operationType='insert',variables=[self.id, self.name, self.email, self.password, self.date],proc='userRegister')

            if queryResult['status'] == 'erro':
                return queryResult

            greenery = Greenery()
            newGreenery = greenery.createGreenery(userId=self.id)

            if newGreenery['status'] =='erro':
                return newGreenery

            return responseHandler.success(content='Usuário cadastrado com sucesso!')
 

        except Exception as error:
            return responseHandler.error(content=str(error))
    
    def _sendEmail(self):
        try:
            sendingEmail = SendEmail()

            email = sendingEmail.sendEmail(token=self.token, email=self.email)
            print(email)

            if email['status'] == 'erro':
                return email
        
            return email
        except Exception as error:
            return responseHandler.error(content=error)
    
    def _setToken(self):
        try:
            self.token = Utils.codeGenerator()

            queryHandler = QueryHandler()

            queryResult = queryHandler.queryExec(operationType='update',variables=[self.email,self.token,Utils.dateCapture(days = 1)], proc='newToken')
            print (queryResult)
            if queryResult['status'] =='erro':
                return queryResult
            
            return responseHandler.success(content='Token cadastrado')
        
        except Exception as error:
            return responseHandler.error(content=error)
        

    def retrieve(self, user):
        try:
            self.email = user
            
            tkn = self._setToken()
            if tkn['status'] == 'erro':
                return tkn
            
            email = self._sendEmail()
            if email['status'] == 'erro':
                return email

            return email
        except Exception as error:
            return responseHandler.error(content=error)

    # def confirmRetrieve(self,user):
    #     try:

    #         return responseHandler.success("")

# user1={
#         "email":"teste2@teste.com",
#         "senha":"teste45",
#         "nome": "ruty"
#     }
# usera=User()

# response = usera.retrieve(user='marllondcsp@gmail.com')
# print(response)


