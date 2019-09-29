from configs import *
from DialogueResponce import DialogueResponce as DR
from enum import Enum
from DialogueMappings import DialogueMappings

class DialogueStates:
    Idle = 1
    Selling = 1


class DialogueHandler:

    def __init__(self, ID):
        self.ID = ID
        self.ttl = bot_ttl  # time to live
        self.state = DialogueStates.Idle

    def get_responce(self, input_str):
        if (input_str in DialogueMappings.keys()):
            if hasattr(self, DialogueMappings[input_str]):
                return getattr(self, DialogueMappings[input_str])()
        else:
            return self.confuse()

    def confuse(self):
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
        return DR.answ_farewell

    def save(self):
        pass

    def load(self):
        pass

if __name__ == "__main__":
    help(DialogueHandler)