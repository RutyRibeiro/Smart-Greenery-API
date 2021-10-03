
if __name__ == 'app.Controllers.PlantController':
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

responserHandler = ResponseHandler()
Utils = utils()

class Plant():
    def __init__(self):
        self.id=''
        self.name=''
        self.date=''
        self.photo=''
        self.idGreen=''
    
    def createPlant(self, plant):
        try:
            validate = Validate()

            validatePlant = validate.validateForm(form=plant, param=['id-estufa','nome-planta'])

            if validatePlant['status'] == 'erro':
                return validatePlant
            
            self.id = Utils.idGenerator()
            self.date = Utils.dateCapture()
            self.name = plant['nome-planta']
            self.idGreen = plant['id-estufa']
            self.photo = 'https://www.svgrepo.com/show/7691/plant.svg'
            
            queryHandler = QueryHandler()

            createPlant = queryHandler.queryExec(operationType='insert', variables=[self.name,self.id, self.date, self.photo, self.idGreen], proc='plantRegister')

            if createPlant['status'] == 'erro':
                return createPlant
        
            return responserHandler.success(content='Planta cadastrada com sucesso!')
        
        except Exception as error:
            return responserHandler.error(content=str(error))

    def deletePlant(self,idPlant):
        try:
            queryHandler = QueryHandler()
            deletePlant = queryHandler.queryExec(operationType='delete', proc='plantDelete', variables=[idPlant])
            
            if deletePlant['status'] == 'error':
                return deletePlant

            return responserHandler.success(content='Planta Deletada com sucesso!')
        
        except Exception as error:
            return responserHandler.error(content=str(error))
    
    def modifyPlant(self,plant):
        try:
            validate = Validate()
            validatePlant = validate.validateForm(form=plant, param=['id-planta','nome-planta'])
            if validatePlant['status'] == 'error':
                return validatePlant
            
            self.id = plant['id-planta']
            self.name = plant['nome-planta']

            getPlant = self.getPlants(idPlant=self.id)

            if getPlant['status'] == 'erro':
                return getPlant
            
            if len(getPlant['mensagem']['conteudo']) == 0:
                raise Exception('Planta não Cadastrada!')

            queryHandler = QueryHandler()
            modifyPlant = queryHandler.queryExec(proc='plantModify',variables=[self.id,self.name], operationType='update')
            
            if modifyPlant['status'] == 'error':
                return modifyPlant
        
            return responserHandler.success(content='Nome alterado com sucesso')
        except Exception as error:
            return responserHandler.error(content=error)
    
    def getPlants(self,idGreen='',idPlant=''):
        try:
            queryHandler = QueryHandler()

            plants = queryHandler.queryExec(operationType='select',variables=[idGreen,idPlant],proc='getPlant')
            
            return plants

        except Exception as error:
            return responserHandler.error(content=error)

# p=Plant()
# print(p.modifyPlant(idGreen='6db7e7cd-98d2-11eb-968d-f5069c8e6f2b'))
    