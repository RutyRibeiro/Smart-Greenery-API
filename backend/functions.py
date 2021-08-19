from mysql.connector import errorcode
import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("LOCAL") == 'dev':
    from connection import openConnection
    from utils import validateLogin, idGenerator, passwordEncode, emailVerify, validateRegister, validateRetrieve, validateGreenRegister,dateCapture, validateElementRegister
    from facialRecognizer import faceRecognition

else:
    from backend.connection import openConnection
    from backend.utils import validateLogin, idGenerator, passwordEncode, emailVerify, validateRegister, validateRetrieve, validateGreenRegister,dateCapture
    from backend.facialRecognizer import faceRecognition


# Função que valida usuário
def login(user):
    data = validateLogin(user)
    
    if data['status'] == 'erro':
        return data
    
    else:

        email = data['user']['email']
        password = data['user']['password']

        conn = openConnection()
       
        if type(conn) == dict:
            return conn

        else:
            try:
                cursor = conn.cursor()

                cursor.callproc('loginTeste', [email,])
                
                for result in cursor.stored_results():
                    row = result.fetchall()

                cursor.close()
                
                if len(row) == 0:
                    raise Exception('Email ou senha incorreto(s)!')
                
                else:
                    idUser = row[0][0]
                    nomeUser = row[0][1]
                    passwordBD = row[0][3]
                    # criptografando senha usando o formato md5
                    passEncode = passwordEncode(password)

                    if passEncode == passwordBD:
                        response = getUser(idUser, nomeUser)
                        return response

                    else:
                        raise Exception('Email ou senha incorreto(s)!')

            except Exception as err:
                return({'message':{'title':'Erro',
                'content': str(err)},
                'status':'erro'})
            
            finally:
                conn.commit()
                conn.close()

# Função que traz informações relacionadas ao usuário depois de validado o login 
def getUser(idUser,nomeUser):
    conn = openConnection()

    if type(conn) == dict:
        return conn
    else:
        try:
            cursor = conn.cursor()

            cursor.callproc('getGreenerys',[idUser])
            data=[]
            
            for result in cursor.stored_results():
                row = result.fetchall()
                for greenery in row:
                    idestufa = greenery[0]
                    greenery={"idestufa": greenery[0],
                            "nomeestufa": greenery[1],
                            "ativo": greenery[2],
                            "dataestufa": greenery[3],
                            "fotoestufa": greenery[4],
                    }
                    cursor.callproc('getElements',[idestufa])
                    elements = []
                    for element in cursor.stored_results():
                        row = element.fetchall()
                        for e in row:
                            elem={"tipoelem": e[0],
                            "nomeelem": e[1],
                            "ativo":e[2]
                            }
                            elements.append(elem)
                    greenery['elementos'] = elements
                    data.append(greenery)
            
            cursor.close()
            return({
                    "status":"ok",
                    "user": nomeUser,
                    "greenerys": data
                    })
        
        except Exception as err:
                return({'message':{'title':'Erro',
                'content': str(err)},
                'status':'erro'})
        finally:
                conn.commit()
                conn.close()

# Função para registrar usuários banco de dados
def register(user):
    conn = openConnection()

    if type(conn) == dict:
        return conn
    
    else:
        try:
            verifiedUser = validateRegister(user)

            if 'status' in verifiedUser:
                return verifiedUser
            else:
                idUser = idGenerator()
                nome = user['name']
                senha = passwordEncode(user['password'])
                data =  dateCapture()
                foto = user['photo']
                email = user['email']
                
                cursor = conn.cursor()

                cursor.callproc('userRegister',[idUser,nome,email,senha,data,foto])

                cursor.close()

                return({'message':{'title':'Sucesso',
                'content':'Usuário cadastrado com sucesso!'},
                'status':'ok'})

        except Exception as err:
            if 'errno' in dir(err):
                if err.errno == 1062:
                    return ({'message':{'title':'Erro',
                    'content': 'Email já cadastrado!'},
                    'status':'erro'})
            else:
                return({'message':{'title':'Erro',
                'content': str(err)},
                'status':'erro'})
        finally:
                conn.commit()
                conn.close()

# Função que verifica o reconhecimento facial para a recuperação de senha do usuário
def retrieve(user):
    try:
        conn = openConnection()
        if type(conn) == dict:
            return conn
        
        verifiedUser = validateRetrieve(user)
        if type(verifiedUser) == dict:
            return verifiedUser
        
        photoUser = user['photouser']
        email = user['email']

        cursor = conn.cursor()

        cursor.callproc('getphoto',[email])

        for result in cursor.stored_results():
            row = result.fetchall()

        photoBD = row[0][0]

        recognition = faceRecognition(photoUser, photoBD)

        if type(recognition) == dict:
            return recognition

        return ('Usuário reconhecido')
        
        cursor.close()
        return ('ok')

    except Exception as error:
        return({'message':{'title':'Erro',
                'content': str(error)},
                'status':'erro'})      
    finally:
                conn.commit()
                conn.close()

# função que registra estufas no banco de dados
def greenregister(green):
    try:
        conn = openConnection()
        if type(conn) == dict:
            return conn

        verifiedGreen = validateGreenRegister(green)
        if type(verifiedGreen) == dict:
            return verifiedGreen

        name = green['name']
        iduser = green['iduser']
        photo = green['photo']
        date = dateCapture()
        idgreen = idGenerator()

        cursor = conn.cursor()
        
        cursor.callproc('greenRegister',[idgreen, name, date, photo, iduser])

        cursor.close()
        return({'message':{'title':'Sucesso',
                'content':'Estufa cadastrada com sucesso!'},
                'status':'ok'})
    
    except Exception as err:
        return({'message':{'title':'Erro',
                'content': str(err)},
                'status':'erro'})
    finally:
        conn.commit()
        conn.close()

# função que registra elementos no banco de dados
def elementregister(element):
    try:
        conn = openConnection()
        print(conn)
        if type(conn) == dict:
            return conn
        
        verifiedelement = validateElementRegister(element)
        if type(verifiedelement) == dict:
            return verifiedelement
        
        idelem = idGenerator()
        nameelem = element['name']
        typeelem = element['type']
        idgreen = element['idgreen']
        date = dateCapture()

        cursor = conn.cursor()
        cursor.callproc('elementRegister',[idelem,typeelem,idgreen,date,nameelem])
        cursor.close()

        return({'message':{'title':'Sucesso',
                'content':'Elemento cadastrado com sucesso!'},
                'status':'ok'})

    except Exception as err:
        return({'message':{'title':'Erro',
            'content': str(err)},
            'status':'erro'})

    finally:
        conn.commit()
        conn.close()

    
