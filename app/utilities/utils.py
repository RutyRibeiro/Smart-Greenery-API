from datetime import datetime,timezone,timedelta
from validate_email import validate_email
import uuid
import hashlib
import string
import random

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
    def dateCapture(self):
        date = (datetime.now().astimezone(timezone(timedelta(hours=-3)))).strftime('%Y/%m/%d')
        return date
    
    # Gera codigo aleatório
    def codeGenerator(self):
        size=8
        chars=string.ascii_uppercase + string.digits
        code = ''.join(random.choice(chars) for _ in range(size))
        return code
