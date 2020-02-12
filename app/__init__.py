from flask import Flask
from flask_mail import Mail

csrf = CSRFProtect()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello friend'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' 
app.config['MAIL_USERNAME'] = '7b8508f6d62ee5'
app.config['MAIL_PASSWORD'] = 'bdb59762a3c0e2'

mail = Mail(app)
csrf.init_app(app)

from app import views
