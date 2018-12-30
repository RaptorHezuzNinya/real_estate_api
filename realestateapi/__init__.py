from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import platform

app = Flask(__name__)
CORS(app)


if platform.system() == 'Darwin':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/real_estate_api' #macOs
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ward:password@localhost/ward' #linux

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from realestateapi import routes
