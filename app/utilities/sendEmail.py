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

    def sendEmail(self, token, email):
        try:
            login = self._loginEmail()
            if login['status'] == 'erro':
                return login
            message = f'''
                        <div style="width:100%;background:#282828;padding:25px 0">
                        <table style=" 
                        border-top:2px solid #0FFF00;
                        margin:0 auto;
                        padding:25px 5px;
                        text-align:center;
                        max-width:620px;width:80%;background:#000; color:#fff;">
                        
                        <tr>
                            <td>Recupere sua conta na <span style="color:#0EAD2B; font-weight:bold">Smart-Greenery</span></td>
                        </tr>
                        <tr>
                            <td>Seu código de acesso é </td>
                        </tr>
                        <tr style="margin-top:25px">
                            <td style="font-size:1.9rem;font-weight:bold">{token}</td>
                        </tr>
                        
                        <tr>
                            <td>
                            Cole este código no aplicativo para recuperar sua senha
                            </td>
                        </tr>
                        
                        </table>
                        </div>
                    '''
            email_msg = MIMEMultipart()
            email_msg['From'] = self.user
            email_msg['To'] = email
            email_msg['Subject'] = 'Recupere sua conta em Smart-Greenery'
            email_msg.attach(MIMEText(message, 'html'))

            self.server.sendmail(
                email_msg['From'], email_msg['To'], email_msg.as_string())
            self.server.quit()

            return responseHandler.success('Email enviado com Sucesso! Verifique sua caixa de entrada ou spam')
        except Exception as error:
            return responseHandler.error(content=error)
