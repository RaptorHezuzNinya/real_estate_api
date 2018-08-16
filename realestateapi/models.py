from flask import render_template, request
from realestateapi import db

class Tenant(db.Model):
    __tablename__ = "tenants"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    account_holder = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(25))    
    last_name = db.Column(db.String(35))    
    iban = db.Column(db.String(35), nullable=False)    
    rent = db.Column(db.Float)
    phone = db.Column(db.String(12))

    def __repr__(self):
        return f"Tenants('{self.id}','{self.firstName}','{self.lastName}','{self.iban}','{self.rent}')"

class Payment(db.Model):
    __tablename__ = "payments"
    id = db.Column(db.Integer, primary_key=True)
    iban = db.Column(db.String(40), nullable=False)    
    rent = db.Column(db.Float, nullable=False)
    account_holder = db.Column(db.String(45), nullable=False)
    payment_json = db.Column(db.JSON, nullable=False)
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