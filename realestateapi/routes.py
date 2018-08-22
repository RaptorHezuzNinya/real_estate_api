from flask import Flask, render_template, request, jsonify
from realestateapi.models import Tenant, Payment, Upload
from realestateapi import app, db
from modules.parser import Parser
import json
import csv
import datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if is_csv(file.filename):
            file.save(
                '/Users/RaptorHezuzNinya/code/python/real_estate_API/uploads/' + file.filename)
            json_list = convert(file.filename)
            return jsonify(json_list)


def convert(filename):
    with open('/Users/RaptorHezuzNinya/code/python/real_estate_API/uploads/' + filename) as csvfile:
        reader = csv.DictReader(csvfile)
        dict_list = []
        for line in reader:
            dict_list.append(line)
        return dict_list


def is_csv(file_name):
    return True if file_name[-3:] == 'csv' else False


# @app.route('/uploadfile', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         json_list = json.load(file)
#         datetime_now = datetime.datetime.now()
#         new_upload = Upload(json_file=json_list, uploaded_at=datetime_now)
#         db.session.add(new_upload)
#         db.session.commit()  # new json upload is now in db;
#         all_uploads_desc = Upload.query.order_by(Upload.id.desc())
#         last_upload = all_uploads_desc.first()
#         p = Parser(last_upload.json_file)
#         p.loop_payments()
#         return jsonify(last_upload.json_file)
