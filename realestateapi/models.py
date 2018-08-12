from flask import render_template, request
from realestateapi import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)

    # def __init__(self, email, password):
    #     self.email = email
    #     self.password = password

    def __repr__(self):
        return f"User('{self.id}','{self.email}')"

class Tenant(db.Model):
    __tablename__ = "tenants"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)    
    firstName = db.Column(db.String(25), nullable=False)    
    lastName = db.Column(db.String(35), nullable=False)    
    iban = db.Column(db.String(35), nullable=False)    
    rent = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Tenants('{self.id}','{self.firstName}','{self.lastName}','{self.iban}','{self.rent}')"

class Payment(db.Model):
    __tablename__ = "payments"
    id = db.Column(db.Integer, primary_key=True)
    iban = db.Column(db.String(40), nullable=False)    
    rent = db.Column(db.Float, nullable=False)
    account_holder = db.Column(db.String(45), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenants.id'), nullable=False)
    
    def __repr__(self):
        return f"Payments('{self.id}', '{self.iban}, '{self.rent}','{self.account_holder}')"

class Upload(db.Model):
    __tablename__ = "uploads"
    id = db.Column(db.Integer, primary_key=True)
    json_file = db.Column(db.JSON)

    def __init__(self, json_file):
        self.json_file = json_file

    def __repr__(self):
        return f"Uploads('{self.id}', '{self.json_file}')"