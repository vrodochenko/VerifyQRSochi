from flask import Flask, request, jsonify, send_file
from qrgen import *
from rsh import *
import json
from CriptoQR import CriptoQR
from SqlTAble import SqlTable

from qrgen import genqr
from rsh import request_exception_handler

# crypto_data = CriptoQR()

app = Flask(__name__)
# ID = 3435435

table = SqlTable()

@app.route("/")
def index():
    return "test"


@app.route('/value', methods=['POST'])
@request_exception_handler
def parse_request():
    req_data = request.get_json()
    # id_dict = {"ID": ID}
    # req_data.update(id_dict)
    print(req_data)
    # req_data = crypto_data.cipher(json.dumps(req_data), crypto_data.key)
    genqr(json.dumps(req_data))
    return "test"
    # TODO:


@app.route('/updatebl', methods=['POST'])
@request_exception_handler
def parse_json():
    req_data = request.get_json()
    for h in req_data['key']:
        table.ban(h)
    return "test"


@app.route('/getfile')
def get_output_file():
    try:
        return send_file('FIO.png', as_attachment=True)
    except Exception as ex:
        message = "Error while processing request: {}".format(ex)
        return message, 429, {'ContentType': 'text/html'}


@app.route("/generate")
@request_exception_handler
def generate():
    genqr("Hello, Nigga")
    return "testqr"


app.run(host="10.178.195.95", port=5000)


def start_server():
    app.run(host="10.178.195.95", port=5000)
