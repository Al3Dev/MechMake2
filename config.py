from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Config:
  SECRET_KEY =  '12345'
  DEBUG      = True

class DevelopmentConfig(Config):
    '''MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'mysql'
    MYSQL_DB = 'mechmake' '''

    #pythonannywere
class DevelopmentConfig(Config):
    MYSQL_HOST = 'ABroStar.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'ABroStar'
    MYSQL_PASSWORD = 'Euri02513'
    MYSQL_DB = 'ABroStar$mechmake'


class MailConfig(Config):
   MAIL_SERVER        = 'smtp.gmail.com'
   MAIL_PORT          = 587
   MAIL_USE_TLS       = True
   MAIL_USE_SSL       = False
   MAIN_USERNAME      = 'alejandro.rodriguez1753@alumnos.udg.mx'
   MAIL_PASSWORD      = 'sdif obmq dlct hsht'
   MAIL_ASCII_ATTACHMENTS = True
   MAIL_DEFAULT_SENDER = 'alejandro.rodriguez1753@alumnos.udg.mx'

config = {
    'development' : DevelopmentConfig,
    'mail'        : MailConfig
  }

