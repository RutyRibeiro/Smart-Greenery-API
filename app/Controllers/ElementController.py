if __name__ == 'app.Controllers.ElementController':
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
            elements = ([Utils.idGenerator(),'Água',idEstufa, Utils.dateCapture(),'Irrigador 1','D0'], 
                        [Utils.idGenerator(),'Água',idEstufa, Utils.dateCapture(),'Irrigador 2','D1'], 
                        [Utils.idGenerator(),'Luz',idEstufa, Utils.dateCapture(),'Luz 1','D2'], 
                        [Utils.idGenerator(),'Luz',idEstufa, Utils.dateCapture(),'Luz 2','D3'], 
                        [Utils.idGenerator(),'Luz',idEstufa, Utils.dateCapture(),'Luz 3','D4'], 
                        [Utils.idGenerator(),'Vento',idEstufa, Utils.dateCapture(),'Ventilador 1','D5'], 
                        [Utils.idGenerator(),'Vento',idEstufa, Utils.dateCapture(),'Ventilador 2','D6']
            )
            queryHandler=QueryHandler()
           
            queryResult = queryHandler.massQueryExec(variables=elements, proc='elementRegister')

            if queryResult['status'] =='erro':
                return queryResult
        
            return responseHandler.success(content='Elementos cadastrados com sucesso!')
        except Exception as error:
            return responseHandler.error(content=str(error))
        
    def modifyElement(self,form):
        try:
            validate = Validate()

            valForm = validate.validateForm(form=form, param=['elemento-id','elemento-nome'])

            if valForm['status'] == 'erro':
                return valForm

            self.name= form['elemento-nome']
            self.id = form['elemento-id']

            queryHandler = QueryHandler()

            modify = queryHandler.queryExec(operationType='update',proc='elementModify', variables=[self.name,self.id])

            if modify['status'] == 'erro':
                return modify
            
            return responseHandler.success(content='Nome do elemento alterado com sucesso!')

        except Exception as error:
            return responseHandler.error(content=str(error))

e = Element()
k = e.createElements(idEstufa='1')
print(k)

