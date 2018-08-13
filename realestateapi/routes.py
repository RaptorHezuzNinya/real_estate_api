from flask import Flask, render_template, request
from realestateapi.models import User, Tenant, Payment, Upload
from realestateapi import app, db
from realestateapi.modules_custom.parser import Parser
import json

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prereg', methods=['GET','POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email, password)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    p = Parser()
    x = p.do_shit()
    return render_template('success.html', var=x)
    

@app.route('/upload', methods=['POST'])
def jsonupload():
        if request.method == 'POST':
            file = request.files['file']
            json_data = json.load(file)
            new_json = Upload(json_data)
            db.session.add(new_json)
            db.session.commit()
            return render_template('success.html', var=file.filename)
