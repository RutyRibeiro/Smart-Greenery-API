import sys
sys.path.append('../')
from app.Handlers.ResponseHandler import ResponseHandler
from app.Handlers.ConnectionHandler import Connection


class QueryHandler():

    def __init__(self):
        self.connection = Connection()
        self.conn = self.connection.openConnection()
        self.cursor = self.conn.cursor()
        self.responseHandler = ResponseHandler()

    def queryExec(self, operationType, variables, proc=None):
        try:
            if proc:
                self.cursor.callproc(proc,variables)

                if operationType =='insert' or operationType =='update' :
                    return self.responseHandler.success(title='Sucesso', content = 'Operação realizada com sucesso!')
                
                else:
                    for result in self.cursor.stored_results():
                        row = result.fetchall() 
                    return row  

        except Exception as error:
            return self.responseHandler.error(title='Erro', content = error)
        
        finally:
            self.cursor.close()
            self.connection.closeConnection(conn=self.conn)
