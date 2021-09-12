class ResponseHandler():
    
    def error(self, content, title = 'Erro!'):
        try:
            resp = {'mensagem': {'titulo': title,
                    'conteudo': content},
                    'status': 'erro'}
            return resp
        
        except:
            return({'mensagem': {'titulo': 'Ops',
                    'conteudo': 'Erro no servidor'},
                    'status': 'erro'})
    
    def success(self, content, title = 'Sucesso!'):
        try:
            resp = {'menssagem': {'titulo': title,
                    'conteudo': content},
                    'status': 'ok'}
            return resp
        except:
            return({'menssagem': {'titulo': 'Ops',
                    'conteudo': 'Erro no servidor'},
                    'status': 'erro'})
            
