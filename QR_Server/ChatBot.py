import configs
import json
from ApiKeys import ApiKeys
import os
import socket
import json
import time

from configs import *

from ApiKeys import *
from ApiResult import ApiResult
from ChatBot import ChatBot
from MessageGenerator import MessageGenerator
from ImageFormat import ImageFormat


class ChatBot:
    def __init__(self, request_id):
        self.auth_token = configs.auth_token
        self.request_id = request_id
        self.message_number_in_queue = 0
        self.socket_to_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.PIC_PATH = configs.PIC_PATH
        self.PIC_THUMB_PATH = configs.PIC_THUMB_PATH

        self.pic = None
        self.pic_thumb = None

    def subscribe_to_messages(self):
        ''' Подписка на сообщение от пользователя
        :param auth_token: токен аутентификации бота
        :param opaque:
        :return: json команды
        '''
        msg = json.dumps({
                ApiKeys.Subscribe: True,
                ApiKeys.Auth: self.auth_token,
                ApiKeys.RequestID: self.message_number_in_queue
            })
        self.socket_to_connect.sendall(bytes(msg, 'utf-8'))
        self.message_number_in_queue += 1

    def connect(self):
        self.socket_to_connect.connect((ip_addr, port))

    def get_pics(self):
        self.pic = None
        self.pic_thumb = None
        with open(self.PIC_PATH, "rb") as f_pic:
            self.my_pic = f_pic.read()
            with open(self.PIC_THUMB_PATH, "rb") as f_pic_thumb:
                self.pic_thumb = f_pic_thumb.read()

    def handle_message(self, encoded_msg):
        if encoded_msg:
            msg = json.loads(encoded_msg)
            if msg.__contains__(ApiKeys.Sender):
                echo_msg = MessageGenerator.create_text_message(auth_token, msg[ApiKeys.Text],
                                                                msg[ApiKeys.Sender],
                                                                self.message_number_in_queue)
                # msg[ApiKeys.Text]
                print(echo_msg)
                self.socket_to_connect.sendall(bytes(echo_msg, 'utf-8'))
                self.message_number_in_queue += 1
                self.get_pics(self)
                echo_image = MessageGenerator.create_image_message(auth_token,
                                                                   msg[ApiKeys.Sender],
                                                                   self.message_number_in_queue,
                                                                   self.pic,
                                                                   self.pic_thumb,
                                                                   ImageFormat.Jpg)
                print(echo_image)
                self.message_number_in_queue += 1
                self.socket_to_connect.sendall(bytes(echo_image, 'utf-8'))
            elif msg.__contains__(ApiKeys.RequestID):  # результат выполнения запроса
                if int(msg[ApiKeys.Result]) != ApiResult.Ok:  # здесь можно обработать ошибки
                    print("error :", msg[ApiKeys.Result])

    def run(self):
        self.connect()
        self.subscribe_to_messages()

        while True:
            data_received = self.socket_to_connect.recv(1024)

            if data_received:
                messages = data_received.split(b"\n")  # we may have more then 1 in the queue, so we split them first
                for encoded_msg in messages:
                    self.handle_message(encoded_msg)

            time.sleep(1)
