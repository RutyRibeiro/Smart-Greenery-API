from time import sleep
if __name__ == 'app.Controllers.GreenerysController':
    from ..Handlers.ResponseHandler import ResponseHandler
    from ..Handlers.QueryHandler import QueryHandler
    from ..utilities.validate import Validate
    from ..utilities.utils import utils
else:
    import sys
    sys.path.append('..')
    from utilities.utils import utils
    from utilities.validate import Validate
    from Handlers.QueryHandler import QueryHandler
    from Handlers.ResponseHandler import ResponseHandler

responseHandler = ResponseHandler()
Utils=utils()

class Element():
    def __init__(self):
        self.id = ''
        self.name = ''
        self.type = ''
        self.active = ''
        self.date = ''
        self.port = ''
    
    def createElements(self, idEstufa):
        try:

            name = ['Irrigador 1','Irrigador 2','Luz 1','Luz 2','Luz 3','Ventilador 1','Ventilador 2']
            port = ['D0','D1','D2','D3','D4','D5','D6','D7']
            tpe = ['Água','Água','Luz','Luz','Luz','Vento','Vento']

            queryHandler=QueryHandler()
            for i in range(7):
                self.id = Utils.idGenerator()
                self.type= tpe[i]
                self.date = Utils.dateCapture()
                self.port = port[i]
                self.name = name[i]
                self.active = '0'
                print(i)
                queryResult = queryHandler.queryExec(operationType='insert',variables=[self.id, self.type, idEstufa, self.date, self.date, self.port], proc='elementRegister')

                if queryResult['status'] =='erro':
                    return queryResult
                
            
            return responseHandler.success(content='Elementos cadastrados com sucesso!')
        except Exception as error:
            return responseHandler.success(content=error)

elements=Element()
print(elements.createElements('1'))

