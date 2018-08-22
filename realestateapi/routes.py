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
            json_list = convert(file)
            return jsonify(output=json_list)


def convert(file):
    # csvfile = open(
    #     '/Users/RaptorHezuzNinya/code/python/real_estate_API/data/smalldata.csv', 'r')
    # jsonfile = []

    # fieldnames = ("Datum", "Naam / Omschrijving", "Rekening", "Tegenrekening",
    #               "Code", "Af Bij", "Bedrag (EUR)", "MutatieSoort", "Mededelingen")
    # reader = csv.DictReader(csvfile, fieldnames)
    # for row in reader:
    #     json.dump(row, jsonfile + ',')
    #     jsonfile.write('\n')
    reader = csv.DictReader(file)
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list


def is_csv(file_name):
    extension = file_name[-3:]
    return True if extension == 'csv' else False


# @app.route('/uploadfile', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         json_data = json.load(file)
#         datetime_now = datetime.datetime.now()
#         new_upload = Upload(json_file=json_data, uploaded_at=datetime_now)
#         db.session.add(new_upload)
#         db.session.commit()  # new json upload is now in db;
#         all_uploads_desc = Upload.query.order_by(Upload.id.desc())
#         last_upload = all_uploads_desc.first()
#         p = Parser(last_upload.json_file)
#         p.loop_payments()
#         return jsonify(last_upload.json_file)
