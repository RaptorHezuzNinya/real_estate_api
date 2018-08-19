from flask import Flask, render_template, request, jsonify
from realestateapi.models import Tenant, Payment, Upload
from realestateapi import app, db
from modules.parser import Parser
import json
import datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        json_data = json.load(file)
        datetime_now = datetime.datetime.now()
        new_upload = Upload(json_file=json_data, uploaded_at=datetime_now)
        db.session.add(new_upload)
        db.session.commit()  # new json upload is now in db;
        all_uploads_desc = Upload.query.order_by(Upload.id.desc())
        last_upload = all_uploads_desc.first()
        p = Parser(last_upload.json_file)
        p.loop_payments()
        return jsonify(last_upload.json_file)


@app.route('/postjson', methods=['POST'])
def post_json():
    if request.method == 'POST':
        # req_content = request.get_json()
        return render_template('postjson.html', var=req_content)
        # return jsonify(req_content)
