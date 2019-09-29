from configs import *


class DialogueHandler:
    def __init__(self, ID):
        self.ID = ID
        self.ttl = bot_ttl  # time to live

    def start(self):
        pass

    def show_help(self):
        answer = \
        '''
        Я продаю билеты в заповедник в Сочи. Я учусь общаться связно, 
        но лучше всего понимаю прямые вопросы:
        
        "купить"
        "почем билеты" или "цена"
        "отмена"
        "что для этого нужно"
        
        Буду рад, если смогу помочь!
        '''
        return answer


    def say_hello(self):
        answer = \
        '''
        Доброе время суток! 
        
        Я могу помочь купить билеты в Сочинский заповедник 
        без очередей и получить QR-код, 
        который можно сохранить на устройстве или распечатать.
        
        Для покупки можно ввести "купить".
        
        Список доступных команд можно получить по слову "помощь" или "?"
        '''
        return answer

    def start_selling():
        answer = \
        '''
        Здорово! Для оформления билета мне понадобятся некоторые Ваши персональные данные.
        
        Они нигде не хранятся и сразу же при получении шифруются. 
        
        Если не согласны -- введите "отмена" или закройте меня. 
        
        Если всё в порядке -- введите ФИО. Следом нужны будут номер паспорта и даты
        поездки.
        '''
        return answer

    def ask_fio(self):
        # Введите ФИО
        pass

    def ask_day_of_birth(self):
        # А теперь дату рождения
        pass

    def ser_num(self):
        # Пожалуйста, введите серию и номер пасспорта
        pass

    def start_of_tour(self):
        # Введите дату вашего прибытия(например 26.09.2019)
        pass

    def finish_of_tour(self):
        # Введите дату педполагаемого завершения тура(например 29.09.2019)
        pass

    def begin_payment(self):
        # Отлично! Пожалуйста, перейдите по ссылке для оплаты
        pass

    def say_bye(self):
        # Сорхание данный QR-код до конца вашего прибывание в заповеднике. Спасибо за обращение, приятного отдыха!
        pass

    def save(self):
        pass

    def load(self):
        pass
