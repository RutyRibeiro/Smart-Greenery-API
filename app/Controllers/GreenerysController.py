if __name__ == 'app.Controllers.GreenerysController':
    from ..Handlers.ResponseHandler import ResponseHandler
    from ..Controllers.ElementController import Element
    from ..Handlers.QueryHandler import QueryHandler
    from ..utilities.validate import Validate
    from ..utilities.utils import utils
else:
    import sys
    sys.path.append('..')
    from utilities.utils import utils
    from utilities.validate import Validate
    from Handlers.QueryHandler import QueryHandler
    from Controllers.ElementController import Element
    from Handlers.ResponseHandler import ResponseHandler


responseHandler= ResponseHandler()
Utils = utils() 

class Greenery():
    def __init__(self):
        self.id=''
        self.name=''
        self.active=''
        self.photo=''
        self.date=''
        self.user_id = ''
    
    def _getElements(self, idEstufa):
        try:
            queryHandler = QueryHandler()

            element = queryHandler.queryExec(operationType='select',variables=[idEstufa],proc='getElements')
            
            if type(element) == dict:
                raise Exception(element['mensagem']['conteudo'])
            
            return element
               
        except Exception as error:
            return responseHandler.error(content=error)
    
    def _formatGreenerys(self,green):
        try:
            data=[] 
            for greenery in green:
                idestufa = greenery[0]
                greenery = {"idestufa": greenery[0],
                            "nomeestufa": greenery[1],
                            "ativo": greenery[2],
                            "dataestufa": greenery[3],
                            "fotoestufa": greenery[4],
                            }
                element = self._getElements(idEstufa=idestufa)
                if type(element) == dict:
                    raise Exception(element['mensagem']['conteudo'])
                
                elements = []
                
                for e in element:
                    elem = {"tipoelem": e[2],
                            "nomeelem": e[5],
                            "ativo": e[1]
                            }
                    elements.append(elem)
                greenery['elementos'] = elements
                data.append(greenery)
            return data
        except Exception as error:
            return responseHandler.error(content=error)
    
    def modifyGreenery(self,form):
        try:
            validate = Validate()

            valForm = validate.validateForm(form=form, param=['estufa-id','estufa-nome'])

            if valForm['status'] == 'erro':
                return valForm

            self.name= form['estufa-nome']
            self.id = form['estufa-id']

            queryHandler = QueryHandler()

            modify = queryHandler.queryExec(operationType='update',proc='greeneryModify', variables=[self.name,self.id])

            if modify['status'] == 'erro':
                return modify
            
            return responseHandler.success(content='Nome da estufa alterado com sucesso!')

        except Exception as error:
            return responseHandler.error(content=error)
    
    def getGreenerys(self, userId):
        try:
            self.user_id = userId

            queryHandler = QueryHandler()
            greenerys = queryHandler.queryExec(operationType='select',variables=[self.user_id],proc='getGreenerys')
            
            if type(greenerys) == dict:
                raise Exception(greenerys['mensagem']['conteudo'])

            formatedGreenerys = self._formatGreenerys(green = greenerys)

            return responseHandler.success(content=formatedGreenerys)

        except Exception as error:
            return responseHandler.error(content=error)
    
    def createGreenery(self, userId):
        try:
            self.user_id = userId
            self.id = Utils.idGenerator()
            self.name = 'Estufa 1'
            self.date = Utils.dateCapture()
            self.photo = 'https://images.pexels.com/photos/5472378/pexels-photo-5472378.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260'

            queryHandler = QueryHandler()
            queryResult = queryHandler.queryExec(operationType='insert',variables=[self.id,self.name,self.date,self.photo,self.user_id], proc='greenRegister')
            
            if queryResult['status']=='erro':
                return queryResult
            
            element = Element()
            newElements = element.createElements(idEstufa=self.id)

            if newElements['status'] == 'erro':
                return newElements
            
            return responseHandler.success(content='Estufa cadastrada com sucesso!')

        except Exception as error:
            return responseHandler.error(content=error)

