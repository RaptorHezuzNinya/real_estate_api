from flask import Flask, render_template, request, jsonify
from realestateapi.models import Tenant, Payment, Upload
from realestateapi import app, db
from modules.parser import Parser
from modules.csv2json import Csv2json
import json
import datetime
import os


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
    return insert_db(json_list)


def handle_json(file):
    json_list = json.load(file)
    return insert_db(json_list)

    # all_uploads_desc = Upload.query.order_by(Upload.id.desc())
    # last_upload = all_uploads_desc.first()
    # p = Parser(last_upload.json_file)
    # p.loop_payments()


def insert_db(payments_json):
    datetime_now = datetime.datetime.now()
    # change column name to something else its list with dict json objects  UPLOAD_CONTENT
    new_upload = Upload(json_file=payments_json, uploaded_at=datetime_now)
    db.session.add(new_upload)
    db.session.commit()  # new js
    return 'sucess uniconr'
