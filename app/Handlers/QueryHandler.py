import mysql.connector
if __name__ == 'app.Handlers.QueryHandler':
    from ..Handlers.ResponseHandler import ResponseHandler
    from ..Handlers.ConnectionHandler import Connection
    
else:
    import sys
    sys.path.append('..')
    from Handlers.ResponseHandler import ResponseHandler
    from Handlers.ConnectionHandler import Connection
  

class QueryHandler():

    def __init__(self):
        self.connection = Connection()
        self.conn = self.connection.openConnection()
        self.cursor = self.conn.cursor()
        self.responseHandler = ResponseHandler()
    
    def massQueryExec(self, variables, proc):
        try:
            for i in range(len(variables)):
                self.cursor.callproc(proc,variables[i])

            return self.responseHandler.success(title='Sucesso', content = 'Operação realizada com sucesso!')
        
        except Exception as error:
            return self.responseHandler.error(content=str(error))
        
        finally:
            self.cursor.close()
            self.connection.closeConnection(conn=self.conn)

    def queryExec(self, operationType, variables, proc=None):
        try:
            if proc:
                self.cursor.callproc(proc,variables)

                if operationType =='select':
                    for result in self.cursor.stored_results():
                        row = result.fetchall() 
                    return self.responseHandler.success(content=row) 
                else:
                    return self.responseHandler.success(title='Sucesso', content = 'Operação realizada com sucesso!')
        
        except mysql.connector.Error as error:
            if error.errno == 1062:
                return self.responseHandler.error(title='Erro', content = 'Email já cadastrado no banco de dados')
            else:
                return self.responseHandler.error(title='Erro', content = error)

        finally:
            self.cursor.close()
            self.connection.closeConnection(conn=self.conn)

