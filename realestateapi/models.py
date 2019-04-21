from realestateapi import db
from sqlalchemy import event, DDL
from sqlalchemy_utils import PasswordType, force_auto_coercion

force_auto_coercion()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
    ),
        unique=False,
        nullable=False,
    )
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(35))
    tenants = db.relationship("Tenant")
    uploads = db.relationship("Uploads")

# here event listener for user 'after-create'


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    account_holder = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(35))
    iban = db.Column(db.String(35), nullable=False)
    rent = db.Column(db.Float)
    phone = db.Column(db.String(12))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'account_holder': self.account_holder,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'iban': self.iban,
            'rent': self.rent,
            'phone': self.phone
        }


# event.listen for Tenant after-create see notes.txt(local)


class Upload(db.Model):
    __tablename__ = "json_upload"
    id = db.Column(db.Integer, primary_key=True)
    upload_content = db.Column(db.JSON)
    uploaded_at = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, upload_content, uploaded_at):
        self.upload_content = upload_content
        self.uploaded_at = uploaded_at

    def __repr__(self):
        return f"Upload('{self.id}', '{self.upload_content}')"


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
