"""
Micro service to send mail with rendered data of Template
"""
__author__ = "Sarath chandra Bellam"

import os

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import cross_origin

from util import find_dividend_in_df
from parserGen import read_sbi_statement

app = Flask(__name__)
# Configuring the port
port = int(os.getenv("PORT", 3001))


ALLOWED_EXTENSIONS = {'pdf', 'excel'}


def is_valid_file_extension(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file_upload', methods=['POST'])
@cross_origin()
def upload_file():
    """

    :return:
    """
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and is_valid_file_extension(file.filename):
        bank = request.args.get("bank", "sbi")
        statement_df = read_sbi_statement(file)
        value = find_dividend_in_df(statement_df, bank)
        resp = jsonify({'dividend' : value})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp





if __name__ == '__main__':
    app.run(port=port)