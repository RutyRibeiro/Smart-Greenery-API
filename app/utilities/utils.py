import time
import uuid
import string
import random
import hashlib
from validate_email import validate_email
from datetime import datetime,timezone,timedelta

# Classe para funções uteis 
class utils():
    # codifica senha no padrão MD5
    def passwordEncode(self, password):
        new_password = hashlib.md5(password.encode())

        return new_password.hexdigest()

    # Gera id unico randomicamente  
    def idGenerator(self):
        newId = str(uuid.uuid1())
        return newId
    
    # verifica se o email informado é valido
    def emailVerify(self, email):
        validate = validate_email(email_address = email, check_regex = True, check_mx = False)
        return validate

    # Captura a data do sistema considerando fuso horario
    def dateCapture(self, days=0):
        date = datetime.now().astimezone(timezone(timedelta(hours=-3, days=days)))
        dateFormat = date.strftime('%Y/%m/%d') 
        return dateFormat
    
    # Gera codigo aleatório
    def codeGenerator(self):
        size=8
        chars=string.ascii_uppercase + string.digits
        code = ''.join(random.choice(chars) for _ in range(size))
        return code
    
    # função para comparar datas
    def compareDates(self,expires):
        date1 = time.strptime(self.dateCapture(), "%Y/%m/%d")
        date2 = time.strptime(expires, "%Y/%m/%d")
        
        return (date1>date2)