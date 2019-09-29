import json
import socket
import time


import configs
from ApiKeys import *
from ImageFormat import ImageFormat
from SeraphimMessage import SeraphimMessage as SM
from SeraphimMessageGenerator import SeraphimMessageGenerator
from configs import *
from DialogieHandler import DialogueHandler


class ChatBot:
    def __init__(self):
        self.auth_token = configs.auth_token
        self.request_id = 0
        self.socket_to_connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.PIC_PATH = configs.PIC_PATH
        self.PIC_THUMB_PATH = configs.PIC_THUMB_PATH

        self.pic = None
        self.pic_thumb = None

        self.DH = DialogueHandler(self.request_id)

    def subscribe_to_messages(self):
        ''' Подписка на сообщение от пользователя
        :param auth_token: токен аутентификации бота
        :param opaque:
        :return: json команды
        '''
        msg = json.dumps({
                ApiKeys.Subscribe: True,
                ApiKeys.Auth: self.auth_token,
                ApiKeys.RequestID: self.request_id
            })
        self.socket_to_connect.sendall(bytes(msg, 'utf-8'))
        self.request_id += 1

    def connect(self):
        self.socket_to_connect.connect((ip_addr, port))

    def get_pics(self):
        self.pic = None
        self.pic_thumb = None
        with open(self.PIC_PATH, "rb") as f_pic:
            self.pic = f_pic.read()
            with open(self.PIC_THUMB_PATH, "rb") as f_pic_thumb:
                self.pic_thumb = f_pic_thumb.read()
        if not self.pic:
            print("Cannot import picture")
        if not self.pic:
            print("Cannot import thumbnail")

    def send_text_message(self, text):
            echo_msg = self.SMG.create_text_message(text)
            self.socket_to_connect.sendall(bytes(echo_msg, 'utf-8'))
            self.request_id += 1

    def send_picture(self, pic, pic_thumb):
        echo_image = self.SMG.create_image_message(image_in_base_64=pic,
                                                   image_thumbnail=pic_thumb,
                                                   image_format=ImageFormat.Jpg)
        self.socket_to_connect.sendall(bytes(echo_image, 'utf-8'))

    def handle_message(self, encoded_msg):
        if encoded_msg:
            msg = json.loads(encoded_msg)
            new_msg = SM(msg)
            self.SMG = SeraphimMessageGenerator(self, new_msg)

            if new_msg.type == "text":
                text_content = msg[ApiKeys.Text]
                print("We received a text message: {}".format(text_content))
                text_in_responce = self.DH.get_responce(text_content)
                print("Responding: {}".format(text_in_responce))
                self.send_text_message(text_in_responce)
                if "пришли QR".lower() in text_content.lower():
                    self.get_pics()
                    self.send_picture(self.pic, self.pic_thumb)
            elif new_msg.type == "server_message":
                print("We have probably received an error: {}".format(msg))
                pass

    def start(self):
        self.connect()
        self.subscribe_to_messages()

    def run(self):
        self.start()
        self.run_main_loop()

    def run_main_loop(self):
        while True:
            data_received = self.socket_to_connect.recv(1024)

            if data_received:
                messages = data_received.split(b"\n")  # we may have more then 1 in the queue, so we split them first
                print("We received {}".format(data_received))
                for encoded_msg in messages:
                    self.handle_message(encoded_msg)
            time.sleep(1)