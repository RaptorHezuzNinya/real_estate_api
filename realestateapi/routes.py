from flask import Flask, render_template, request, jsonify
from realestateapi.models import Tenant, Payment, Upload
from realestateapi import app, db
from realestateapi.modules.parser import Parser
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

@app.route('/uploadfile', methods=['POST'])
def upload_file():
        if request.method == 'POST':
            file = request.files['file']
            json_data = json.load(file) # list containing json object (in python dictionaries)
            json_dump = json.dumps(json_data)
            # return render_template('uploadfile.html', var=json_dump)
            return jsonify(json_data)
            
            # works -> 
            # json_data = json.load(file)
            # new_json = Upload(json_data)
            # db.session.add(new_json)
            # db.session.commit()
            # return render_template('success.html', var=file.filename)

@app.route('/postjson', methods=['POST'])
def post_json():
        if request.method == 'POST':
            req_content = request.get_json()
            return render_template('postjson.html', var=req_content)
            # return jsonify(req_content)
            