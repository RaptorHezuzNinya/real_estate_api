from flask import Flask, render_template, request, jsonify
from realestateapi.models import Tenant, Payment, Upload
from realestateapi import app, db
from modules.parser import Parser
from modules.csv2json import Csv2json
import json
import datetime
import os


@app.route('/tenants')
def get_tenants():
    tenant = Tenant()
    tenants = tenant.query.all()
    return jsonify([t.serialize for t in tenants])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']

        if is_csv(file.filename):
            cwd = os.getcwd()
            path = cwd + '/uploads/' + file.filename

            save_file(file, path)

            return handle_csv(path)

        return handle_json(file)


def save_file(file, path):
    return file.save(path)  # file is saved to uploads dir


def is_csv(file_name):
    return True if file_name[-3:] == 'csv' else False


def handle_csv(path):
    c2j = Csv2json(path)
    json_list = c2j.get_json()
    insert_db(json_list)
    return run_parser()


def handle_json(file):
    json_list = json.load(file)
    insert_db(json_list)
    return run_parser()


def run_parser():
    last_upload = get_last_upload()
    p = Parser(last_upload.upload_content)
    p.loop_payments()
    return 'parsing complete'


def insert_db(payments_json):
    datetime_now = datetime.datetime.now()
    new_upload = Upload(upload_content=payments_json, uploaded_at=datetime_now)
    db.session.add(new_upload)
    db.session.commit()
    return 'upload successful'


def get_last_upload():
    all_uploads_desc = Upload.query.order_by(Upload.id.desc())
    last_upload = all_uploads_desc.first()
    return last_upload
