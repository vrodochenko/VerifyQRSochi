import io
from flask import Flask, request, jsonify, send_file
from qrgen import *
from rsh import *
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "test"


@app.route('/value', methods=['POST'])
@request_exception_handler
def parse_request():
    req_data = request.get_json()
    print(str(req_data))
    genqr("ФИО: " + req_data["FIO"] + "\n" +
          "Дата рождения: " + req_data["Day_of_birth"] + "\n" +
          "Серия и номер паспорта: " + req_data["Ser_num"] + "\n" +
          "Начало тура: " + req_data["Start_of_tour"] + "\n" +
          "Окончание тура: " + req_data["Finish_of_tour"] + "\n")

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


if __name__ == "__main__":
    app.run(host = "10.178.195.95", port=5000)
