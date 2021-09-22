import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
if __name__ == 'app.utilities.sendEmail':
    from ..Handlers.ResponseHandler import ResponseHandler
else:
    import sys
    sys.path.append('..')
    from Handlers.ResponseHandler import ResponseHandler
responseHandler = ResponseHandler()

load_dotenv()

class SendEmail():
    
    def __init__(self):
            self.host = os.getenv("EMAILHOST")
            self.port = os.getenv("EMAILPORT")
            self.user = os.getenv("EMAILUSER")
            self.password = os.getenv("EMAILPASSWORD")
            self.server = smtplib.SMTP(self.host, self.port)

    def _loginEmail(self):
        try:
            self.server.ehlo()
            self.server.starttls()
            self.server.login(self.user, self.password)
            return responseHandler.success(content='Login Realizado')

        except Exception as error:
            return responseHandler.error(content=error)

    def sendEmail(self,token,email):
        try:
            login = self._loginEmail()
            if login['status'] == 'erro':
                return login
            message = f'''
                            <div style="textAlign:center">
                            <h2>Olá recupere sua conta Smart-Greenery</h2>
                            <h4>Seu código de acesso é {token}</h4>
                            
                            </div>
                    '''
            email_msg = MIMEMultipart()
            email_msg['From'] = self.user
            email_msg['To'] = email
            email_msg['Subject'] = 'SMART-GREENERY - Recuperação de Conta'
            email_msg.attach(MIMEText(message, 'html'))

            self.server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            self.server.quit()

            return responseHandler.success('Email enviado com Sucesso!')
        except Exception as error:
            return responseHandler.error(content=error)

em = SendEmail()
print(em.sendEmail(token='213124234',email='rribeiropena@gmail.com'))