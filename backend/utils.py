from datetime import datetime,timezone,timedelta
from validate_email import validate_email
import uuid
import hashlib
import cv2
from dotenv import load_dotenv
import os

load_dotenv()


if os.getenv("LOCAL") == 'dev':
    from facialRecognizer import faceDetect
else:
    from backend.facialRecognizer import faceDetect


# valida form de login de usuário
def validateLogin(user):
    try:
        if 'email' in user and 'password' in user:
            
            email = user['email']
            password = user['password']

            if (email is None or email == ''):
                raise Exception('Email não informado!')
            
            elif not(emailVerify(email)):
                raise Exception('E-mail não valido!')
        
            elif (password is None or password == '') :
                raise Exception('Senha não informado!')
            
            else:
                return({
                    "status":"ok",
                    "message":"validado",
                    "user":{
                        "email": email,
                        "password": password
                        }
                    })
        else:
            raise Exception('E-mail ou senha inexistente!')

    except Exception as error:
        
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

# valida form de registro de usuário
def validateRegister(user):
    try:
        if 'email' in user and 'password' in user and 'name' in user and 'photo' in user:
            
            email = user['email']
            password = user['password']
            name = user['name']
            photo = user['photo']
            detect=faceDetect(photo)

            if (email is None or email == ''):
                raise Exception('Email não informado!')
            
            elif not(emailVerify(email)):
                raise Exception('E-mail não valido!')
            
            elif (name is None or name == ''):
                raise Exception('nome não informado!')
            
            elif (photo is None or photo == ''):
                raise Exception('foto não informada!')
            
            elif (detect != 1):
                raise Exception('Não encontramos um rosto, tente novamente!')
            
            elif (password is None or password == '') :
                raise Exception('Senha não informado!')
            
            else:
                return('ok')
        else:
            raise Exception('Alguma informação não foi passada!')

    except Exception as error:
        
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

# valida form de recuperação de senha 
def validateRetrieve(user):
    try:
        if 'email' in user and 'photouser' in user:
            
            email = user['email']
            photoUser = user['photouser']

            if (email is None or email == ''):
                raise Exception('Email não informado!')
            
            elif (photoUser is None or photoUser == ''):
                raise Exception('Foto não informada!') 
            else:
                return 'ok'
        else:
            raise Exception('Email ou Foto não informados!')
    except Exception as error:
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

# valida form de registro de estufa
def validateGreenRegister(green):
    try:
        if 'name' in green and 'iduser' in green and 'photo' in green:
            
            name = green['name']
            iduser = green['iduser']
            photo = green['photo']

            if (name is None or name == ''):
                raise Exception('Nome não informado!')
            
            elif (photo is None or photo == ''):
                raise Exception('Foto não informada!') 
            
            elif (iduser is None or iduser == ''):
                raise Exception('Id de usuário não informado!') 
            else:
                return 'ok'
        else:
            raise Exception('nome, id ou/e foto não informados!')
    except Exception as error:
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

# valida form de registro de elemento
def validateElementRegister(element):
    try:
        if 'name' in element and 'type' in element and 'idgreen' in element:
            name = element['name']
            typeelem = element['type']
            idgreen = element['idgreen']
        
            if (name is None or name == ''):
                raise Exception('Nome do elemento não informado!')
        
            if (typeelem is None or typeelem == ''):
                raise Exception('Tipo do elemento não informado!')
        
            if (idgreen is None or idgreen == ''):
                raise Exception('id da estufa não informado!')

            else: 
                return 'ok'
        else:
            raise Exception('nome, id ou/e foto não informados!')
    except Exception as error:
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})

# codifica senha no padrão MD5
def passwordEncode(password):
    new_password = hashlib.md5(password.encode())

    return new_password.hexdigest()

# Gera id unico randomicamente  
def idGenerator():
    newId = str(uuid.uuid1())
    return newId

# verifica se o email informado é valido
def emailVerify(email):
    validate = validate_email(email_address = email, check_regex = True, check_mx = False)
    return validate

# Captura a data do sistema considerando fuso horario
def dateCapture():
    date = (datetime.now().astimezone(timezone(timedelta(hours=-3)))).strftime('%Y/%m/%d')
    return date