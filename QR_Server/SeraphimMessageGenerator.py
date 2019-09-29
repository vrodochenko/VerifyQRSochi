from ApiKeys import ApiKeys
from MimeTypes import MimeTypes
import json
from base64 import b64encode
from ReceiverEncodings import ReceiverEncodings


class SeraphimMessageGenerator:

    def __init__(self, chat_bot, incoming_msg):
        self.auth_token = chat_bot.auth_token
        self.receiver = incoming_msg.sender
        self.request_id = chat_bot.request_id

    def create_text_message(self, text):
        '''
        Создание текстового сообщения
        :param auth_token: токен аутентификации бота
        :param text: Текст сообщения
        :param receiver: sha-256 хэш-сумма логина получателя
        :param opaque: идентификатор запроса к API. Число
        :return: json команды
        '''

        text_message_to_send = json.dumps(
            {
                ApiKeys.Text: text,
                ApiKeys.MimeType: MimeTypes.Text,
                ApiKeys.Receiver: self.receiver,
                ApiKeys.RequestID: self.request_id,
                ApiKeys.ReceiverEncoding: ReceiverEncodings.Hash,
                ApiKeys.Auth: self.auth_token},
            separators=(',', ':')
        )

        return text_message_to_send

    def create_image_message(self, image_in_base_64, image_thumbnail, image_format):
        '''
        Создание сообщения с изображением
        :param auth_token: токен аутентификации бота
        :param receiver: sha-256 хэш-сумма логина получателя
        :param opaque: идентификатор запроса к API. Число
        :param image: изображение, закодированное в base64
        :param image_thumbnail: миниатюра изображения, закодированная в base64
        :param image_format: формат изображения
        :return: json команды
        '''
        return json.dumps(
            {
                ApiKeys.MimeType: MimeTypes.Image,
                ApiKeys.Receiver: self.receiver,
                ApiKeys.RequestID: self.request_id,
                ApiKeys.ReceiverEncoding: ReceiverEncodings.Hash,
                ApiKeys.Image: b64encode(image_in_base_64).decode(),
                ApiKeys.ImageThumbnail: b64encode(image_thumbnail).decode(),
                ApiKeys.ImageFormat: image_format,
                ApiKeys.Auth: self.auth_token},
            separators=(',', ':')
        )
