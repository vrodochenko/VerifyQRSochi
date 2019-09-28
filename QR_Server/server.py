import io
from flask import Flask, request, jsonify, send_file
from qrgen import *
from rsh import *
import json

from qrgen import genqr
from rsh import request_exception_handler

app = Flask(__name__)


@app.route("/")
def index():
    return "test"


@app.route('/value', methods=['POST'])
@request_exception_handler
def parse_request():
    req_data = request.get_json()
    genqr(json.dumps(req_data))
    return "test"
    # TODO:


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


def start_server():
    app.run(host="10.178.195.95", port=5000)
