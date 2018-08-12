class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email):
        self.email = email

    # def __repr__(self):
    #     return '<E-mail %r>' % self.email

    def __repr__(self):
        return f"Tenant('{self.id}','{self.email}')"

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(25), nullable=False)    
    lastName = db.Column(db.String(35), nullable=False)    
    iban = db.Column(db.String(35), nullable=False)    
    rent = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Tenant('{self.id}','{self.firstName}','{self.lastName}','{self.iban}','{self}')"

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    iban = db.Column(db.String(40), nullable=False)    
    rent = db.Column(db.Float, nullable=False)
    account_holder = db.Column(db.String(45), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    
    def __repr__(self):
        return f"Stub('{self.id}', '{self.iban}, '{self.rent}','{self.account_holder}')"
    