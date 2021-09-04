class ResponseHandler():
    
    def error(self, title, content):
        try:
            resp = {'message': {'title': title.captalize(),
                    'content': content.captalize()},
                    'status': 'erro'}
            return resp
        
        except:
            return({'message': {'title': 'Ops',
                    'content': 'Erro no servidor'},
                    'status': 'erro'})
    
    def success(self, title, content):
        try:
            resp = {'message': {'title': title.captalize(),
                    'content': content.captalize()},
                    'status': 'ok'}
            return resp
        except:
            return({'message': {'title': 'Ops',
                    'content': 'Erro no servidor'},
                    'status': 'erro'})
            
