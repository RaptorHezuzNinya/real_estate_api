from flask import Flask, render_template, request
from realestateapi.models import User, Tenant, Payment, Upload
from realestateapi import app, db

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/prereg', methods=['POST'])
# def prereg():
#     email = None
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         # Check that email does not already exist (not a great query, but works)
#         if not db.session.query(User).filter(User.email == email).count():
#             reg = User(email, password)
#             db.session.add(reg)
#             db.session.commit()
#             return render_template('success.html')
#     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def jsonupload():
    if request.method == 'POST':
        json_upload = request.get_json()
        new_upload = Upload(json_upload)
        db.session.add(new_upload)
        db.session.commit()
        return render_template('success.html')