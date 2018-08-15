from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event, DDL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/real_estate_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from realestateapi import routes
from realestateapi.models import Tenant

event.listen(Tenant.__table__, 'after_create', DDL(""" INSERT INTO tenants (email, first_name, last_name, iban, rent, phone) VALUES ('test@email', 'ward', 'verhoef', 'nl44ingb0009399983', 344.8, '0658707056')"""))
