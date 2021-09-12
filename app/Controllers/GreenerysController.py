if __name__ == 'app.Controllers.GreenerysController':
    from ..Handlers.ResponseHandler import ResponseHandler
    from ..Handlers.QueryHandler import QueryHandler
    from ..utilities.validate import Validate
else:
    import sys
    sys.path.append('..')
    from utilities.validate import Validate
    from Handlers.QueryHandler import QueryHandler
    from Handlers.ResponseHandler import ResponseHandler

responseHandler= ResponseHandler()

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

# greenery=Greenery()

# print(greenery.modifyGreenery({
#     'estufa-nome':'teste',
#     'estufa-id':'1'
# }))


