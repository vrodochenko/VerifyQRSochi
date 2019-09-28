import socket
import json
import time
from os.path import dirname, realpath
from ApiKeys import *
from ApiResult import ApiResult
from ChatBot import ChatBot
from MessageGenerator import MessageGenerator
from ImageFormat import ImageFormat

from base64 import b64encode
from sys import argv, exit

PIC_PATH = dirname(realpath(__file__)) + "/FIO.png"
PIC_THUMB_PATH = dirname(realpath(__file__)) + "/FIO.png"
OPAQUE = 0

ip_addr = 'api.seraphim.online'
port = 20001
auth_token = 'b18abcd5af40ae5dec47bdff580475f2bd5f96356896cf2965fbd281ea27448b'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sock)
sock.connect((ip_addr, port))
msg = ChatBot.subscribe_to_messages(auth_token, OPAQUE)
print(msg)
sock.sendall(bytes(msg, 'utf-8'))
OPAQUE += 1
pic = None
pic_thumb = None
with open(PIC_PATH, "rb") as f_pic:
    pic = f_pic.read()
    with open(PIC_THUMB_PATH, "rb") as f_pic_thumb:
        pic_thumb = f_pic_thumb.read()

while True:
    data = sock.recv(1024)

    if data:
        print('Received', data)
        # Так как мы вычитываем раз в секунду, у нас может накопиться несколько сообщений от сервера:
        # {"opaque": 2,  "result": 0}\n{"opaque": 3,  "result": 0}\n
        # необходимо их разделить перед передачей в парсер
        messages = data.split(b"\n")
        print(messages)
        for encoded_msg in messages:
            if encoded_msg:
                msg = json.loads(encoded_msg)
                if msg.__contains__(ApiKeys.Sender):  # входящее сообщение от пользователя
                    echo_msg = MessageGenerator.create_text_message(auth_token, "чё?", msg[ApiKeys.Sender], OPAQUE)
                    # msg[ApiKeys.Text]
                    print(echo_msg)
                    sock.sendall(bytes(echo_msg, 'utf-8'))
                    OPAQUE += 1
                    echo_image = MessageGenerator.create_image_message(auth_token, msg[ApiKeys.Sender], OPAQUE, pic,
                                                      pic_thumb, ImageFormat.Jpg)
                    print(echo_image)
                    OPAQUE += 1
                    sock.sendall(bytes(echo_image, 'utf-8'))
                elif msg.__contains__(ApiKeys.OpaqueData):  # результат выполнения запроса
                    if int(msg[ApiKeys.Result]) != ApiResult.Ok:  # здесь можно обработать ошибки
                        print("error :", msg[ApiKeys.Result])

    time.sleep(1)
