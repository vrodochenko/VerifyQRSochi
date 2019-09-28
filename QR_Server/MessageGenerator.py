import json
from ApiKeys import ApiKeys
from MimeTypes import MimeTypes
import json
from base64 import b64encode
from ReceiverEncodings import ReceiverEncodings


class MessageGenerator:

    @staticmethod
    def create_text_message(auth_token, text, receiver, opaque):
        '''
        Создание текстового сообщения
        :param auth_token: токен аутентификации бота
        :param text: Текст сообщения
        :param receiver: sha-256 хэш-сумма логина получателя
        :param opaque: идентификатор запроса к API. Число
        :return: json команды
        '''

        return json.dumps(
            {ApiKeys.Text: text,
             ApiKeys.MimeType: MimeTypes.Text,
             ApiKeys.Receiver: receiver,
             ApiKeys.OpaqueData: opaque,
             ApiKeys.ReceiverEncoding: ReceiverEncodings.Hash,
             ApiKeys.Auth: auth_token}, separators=(',', ':'))

    @staticmethod
    def create_image_message(auth_token, receiver, opaque, image, image_thumbnail, image_format):
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
            {ApiKeys.MimeType: MimeTypes.Image,
             ApiKeys.Receiver: receiver,
             ApiKeys.OpaqueData: opaque,
             ApiKeys.ReceiverEncoding: ReceiverEncodings.Hash,
             ApiKeys.Image: b64encode(image).decode(),
             ApiKeys.ImageThumbnail: b64encode(image_thumbnail).decode(),
             ApiKeys.ImageFormat: image_format,
             ApiKeys.Auth: auth_token}, separators=(',', ':'))
