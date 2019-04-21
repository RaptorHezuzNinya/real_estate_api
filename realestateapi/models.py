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


event.listen(User.__table__, 'after_create',
             DDL(""" INSERT INTO "user" (email, password, first_name, last_name) VALUES ('ward.verhoef@gmail.com', 'password', 'ward', 'verhoef')  """))


class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    account_holder = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(35))
    iban = db.Column(db.String(35), nullable=False)
    rent = db.Column(db.Float)
    phone = db.Column(db.String(12))

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

    # def __repr__(self):
    #     return f"Tenant('{self.id}','{self.account_holder}', '{self.first_name}','{self.last_name}','{self.iban}','{self.rent}','{self.phone}')"
