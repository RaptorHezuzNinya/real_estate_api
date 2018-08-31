from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/real_estate_api' #macOs
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ward:password@localhost/ward'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from realestateapi import routes
