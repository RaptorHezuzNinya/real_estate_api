from realestateapi import db
from sqlalchemy import event, DDL


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iban = db.Column(db.String(40), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    account_holder = db.Column(db.String(150), nullable=False)
    payment_json = db.Column(db.JSON, nullable=False)
    date = db.Column(db.Date, nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey(
        'tenant.id'), nullable=False)

    def __repr__(self):
        return f"Payment('{self.id}', '{self.iban}, '{self.rent}','{self.account_holder}')"


class Upload(db.Model):
    __tablename__ = "json_upload"
    id = db.Column(db.Integer, primary_key=True)
    json_file = db.Column(db.JSON)
    uploaded_at = db.Column(db.Date)

    def __init__(self, json_file, uploaded_at):
        self.json_file = json_file
        self.uploaded_at = uploaded_at

    def __repr__(self):
        return f"Upload('{self.id}', '{self.json_file}')"
