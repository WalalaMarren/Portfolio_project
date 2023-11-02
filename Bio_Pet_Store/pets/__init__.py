from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2c5eaf5defac18ee6fd490c7a8f89b7c13ae707'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

app.app_context().push()

#bcrypt = Bcrypt(app)
from pets import routes