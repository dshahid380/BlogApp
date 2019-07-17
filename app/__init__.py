from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0e488ff4a21afe9fe5ac5fb68f7bd68'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
<<<<<<< HEAD
=======

>>>>>>> 821136f03ecba87f8c4d39361c6e9bf88f988d97

from app import routes