from mysql.connector import connect, errorcode
import os
import connection
import utils

class User():

    def __init__(self):
        self.id = ''
        self.email =''
        self.password =''
        self.name=''
        self.date=''
    
    def _validateUserLogin(self, user):
        try:
            valida=utils.Validate()
            
            param = ['email','senha']
            validate = valida.validateForm(form = user, param = param)

            if validate['status'] =='erro':
                raise Exception(validate['message']['content'])

            self.email=user['email']
            self.password=user['senha']           

            return validate
        
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

    def _openAndValidateConnection(self):
        connect = connection.Connection()

        conn = connect.openConnection()
        
        return conn
    
    def _closeConnection(self,conn):
        connect = connection.Connection()
        
        connect.closeConnection(conn=conn)
    
    def _getUserDB(self):
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
            
            return ({'message':{'title':'sucesso',
                'content': 'Usuário existente no banco de dados'},
                'status':'ok'})
        
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})
    
    def login(self, user):
        try:
            validate = self._validateUserLogin(user=user)

            if validate['status'] == 'erro':
                raise Exception(validate['message']['content'])
            
            getUser = self._getUserDB()

            if getUser['status'] == 'erro':
                raise Exception(getUser['message']['content'])
                
            return getUser
            
        except Exception as error:
            return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})


user1={
        "email":"teste@teste.com",
        "senha":"123"
    }
usera=User()

response = usera.login(user=user1)
print(response)


