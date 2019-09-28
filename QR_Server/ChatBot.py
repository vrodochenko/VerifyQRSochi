import json
from ApiKeys import ApiKeys


class ChatBot:
    def subscribe_to_messages(auth_token, opaque):
        ''' Подписка на сообщение от пользователя
        :param auth_token: токен аутентификации бота
        :param opaque:
        :return: json команды
        '''
        return json.dumps(
            {
                ApiKeys.Subscribe: True,
                ApiKeys.Auth: auth_token,
                ApiKeys.OpaqueData: opaque
            }
        )