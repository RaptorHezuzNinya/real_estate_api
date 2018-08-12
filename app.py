from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/realEstateApi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(25), nullable=False)    
    lastName = db.Column(db.String(35), nullable=False)    
    iban = db.Column(db.String(35), nullable=False)    
    rent = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Tenant('{self.id}','{self.firstName}','{self.lastName}','{self.iban}','{self}')"

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()


# class Stub(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150))
#     post = db.Column(db.String(500))

#     def __repr__(self):
#         return '<Tenant %r>' % self.id, self.title, self.post
#         # return f"Stub('{self.id}', '{self.title}, '{self.post}')"


# class Payment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     iban = db.Column(db.String(40), nullable=False)    
#     rent = db.Column(db.Float, nullable=False)
#     account_holder = db.Column(db.String(45), nullable=False)
#     tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'), nullable=False)
    
#     def __repr__(self):
#         return f"Stub('{self.id}', '{self.iban}, '{self.rent}','{self.account_holder}')"
    