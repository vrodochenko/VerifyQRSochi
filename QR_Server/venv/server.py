import io
from flask import Flask, request, jsonify, send_file
from qrgen import*
from rsh import*
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
    genqr(str(req_data))
    # TODO:


@app.route('/getfile')
def get_output_file():
    try:
        print(send_file('FIO.png', mimetype='image/gif').__dict__)
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
   app.run()