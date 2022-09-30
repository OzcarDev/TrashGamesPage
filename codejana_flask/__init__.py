
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SECRET_KEY']  = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/cjflask.db'

db=SQLAlchemy(app)
from codejana_flask import routes








