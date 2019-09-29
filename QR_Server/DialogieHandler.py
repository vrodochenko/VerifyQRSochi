from configs import *
from DialogueResponce import DialogueResponce as DR
from DialogueMappings import DialogueMappings

class DialogueStates:
    Idle = 0
    Selling = 1
    GettingPassport = 2
    GettinStartDates = 3
    GettingEndDates = 4


class DialogueHandler:

    def __init__(self, ID):
        self.ID = ID
        self.ttl = bot_ttl  # time to live
        self.state = DialogueStates.Idle

    def get_responce(self, input_str):
        if self.state == DialogueStates.Idle:  # there's nothing we trade
            return self.get_chatting_responce(input_str)
        elif self.state == DialogueStates.Selling:  # want to collect the name
            return DR.answ_selling_error

    def get_chatting_responce(self, input_str):
        input_str = input_str.lower() # don't want to be case-sensitive
        # We are not selling, just communicating:
        if (input_str in DialogueMappings.keys()):
            if hasattr(self, DialogueMappings[input_str]):
                return getattr(self, DialogueMappings[input_str])()
        else:
            return self.confuse()

    def get_passport_responce(self, input_str):
        return DR.answ_ask_passport

    def get_start_date_responce(self, input_str):
        return DR.answ_ask_start_date

    def get_end_date_responce(self, input_str):
        return DR.answ_ask_end_date

    def confuse(self):
        if self.state != DialogueStates.Idle:
            return DR.answ_selling_error
        return DR.answ_unknown

    def reset_state(self):
        self.state = DialogueStates.Idle
        return DR.answ_cancel

    def show_help(self):
        return DR.answ_help

    def show_price(self):
        return DR.answ_price

    def say_hello(self):
        return DR.answ_hello

    def start_selling(self):
        self.state = DialogueStates.Selling
        return DR.answ_start_selling

    def ask_tour_start(self):
        return DR.answ_ask_start_date

    def ask_tour_stop(self):
        return DR.answ_ask_end_date

    def begin_payment(self):
        return DR.answ_ask_for_payment

    def say_bye(self):
        self.state = DialogueStates.Idle
        return DR.answ_bye

    def finish_procedures(self):
        self.state = DialogueStates.Idle
        return DR.answ_farewell

    def save(self):
        pass

    def load(self):
        pass

if __name__ == "__main__":
    help(DialogueHandler)