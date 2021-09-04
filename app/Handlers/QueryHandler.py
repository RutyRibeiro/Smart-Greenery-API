import sys
sys.path.append('../')
from mysql.connector import connection
from connection import Connection
from utils import utils
from ResponseHandler import ResponseHandler

class QueryHandler():

    def __init__(self):
        self.connection = Connection()
        self.conn = self.connection.openConnection()
        self.cursor = self.conn.cursor()

    def queryExec(self, operationType, variables, proc=None):
        responseHandler=ResponseHandler()
        try:
            if proc:
                self.cursor.callproc(proc,variables)

                if operationType =='insert' or operationType =='update' :
                    return responseHandler.success(title='Sucesso', content = 'Operação realizada com sucesso!')
                
                else:
                    for result in self.cursor.stored_results():
                        row = result.fetchall() 
                    return row  

        except Exception as error:
            return responseHandler.error(title='Erro', content = error)
        
        finally:
            self.cursor.close()
            self.connection.closeConnection(conn=self.conn)

date= utils()
execquery = QueryHandler()
# print(execquery.queryExec(proc='userRegister',operationType='insert',variables=['assassde','teste','ro@teste.com','123',date.dateCapture(),'https://via.placeholder.com/150']))
print(execquery.queryExec(operationType='select',proc='loginTeste',variables=['r',]))
    
    

    
