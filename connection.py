import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class Connection():
    # define dados refentes ao banco de dados
    def __init__(self):
        self.config = {
            'host' : os.getenv("HOST"),
            'port' : os.getenv("DBPORT"),
            'database' : os.getenv("DATABASE"),
            'user': os.getenv("DBUSER"),
            'password': os.getenv("PASSWORD"),
            'ssl_disabled': True
            # 'host' : os.environ.get("HOST"),
            # 'port' : os.environ.get("DBPORT"),
            # 'database' : os.environ.get("DATABASE"),
            # 'user': os.environ.get("DBUSER"),
            # 'password': os.environ.get("PASSWORD"),
            # 'ssl_disabled': True
        }

    def openConnection(self):
        try:
            conn = mysql.connector.connect(**self.config)

            print("Acesso ao banco de dados: Conexão Estabelecida")
        except mysql.connector.Error as err:
            return({'status':'erro', 'message': 'Falha na conexão com o banco de dados'})
        else:
            return conn
    
    def closeConnection(self, conn):
        try:
            conn.commit()
            conn.close()
            print("Conexão com banco de dados encerrada")
        except:
            print("Falha ao encerrar conexão com banco de dados")





    
        