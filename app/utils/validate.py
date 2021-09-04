import sys
sys.path.append('../')
from app.Handlers import ResponseHandler
class Validate():

    def __init__(self):
        self.param = []
        self.form = {}
        self.responseHandler = ResponseHandler.ResponseHandler()

    
    def _verifyExistance(self):
        try:
            for field in self.param:
                if field not in self.form:
                    raise Exception(f"O campo {field} é inexistente")
            
            return self.responseHandler.success(title='Sucesso',content='Campos validados com sucesso')

        except Exception as error:
            return self.responseHandler.error(title='Erro',content=str(error))

    def _verifyIsEmpty(self):
        try:
            for field in self.param:
                if self.form[field] is None or self.form[field] =='':
                    raise Exception(f"O campo {field} está vazio")
                
            return self.responseHandler.success(title='Sucesso',content='Campos validados com sucesso')

        except Exception as error:
            return self.responseHandler.error(title='Erro',content=str(error))

    def validateForm(self,form,param):
        self.param= param
        self.form = form

        verifyExistance = self._verifyExistance()

        if verifyExistance['status'] == 'erro':
            return verifyExistance
        
        return self._verifyIsEmpty()
