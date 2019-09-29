from configs import *
from DialogueResponce import DialogueResponce as DR
from DialogueMappings import DialogueMappings
from Person import Person


class DialogueStates:
    Idle = 0
    Selling = 1
    GettingPassport = 2
    GettingBirthDate = 3
    GettingStartDate = 4
    GettingEndDate = 5
    Finish = 6


class DialogueHandler:

    def __init__(self, ID):
        self.ID = ID
        self.ttl = bot_ttl  # time to live
        self.State = DialogueStates.Idle
        self.Pers = Person()

    def get_responce(self, input_str):
        input_str = input_str.lower()
        if self.State == DialogueStates.Idle:  # there's nothing we trade
            return self.get_chatting_responce(input_str)
        else:
            self.populate_person(input_str)
            if self.State == DialogueStates.GettingPassport:
                return self.get_passport_responce()
            if self.State == DialogueStates.GettingBirthDate:
                return self.get_birth_date_responce()
            if self.State == DialogueStates.GettingStartDate:
                return self.get_start_date_responce()
            if self.State == DialogueStates.GettingEndDate:
                return self.get_end_date_responce()
            if self.State == DialogueStates.Finish:
                return self.get_success_responce()
            else:
                return DR.get_chatting_responce()

    def get_chatting_responce(self, input_str):
        input_str = input_str.lower() # don't want to be case-sensitive
        # We are not selling, just communicating:
        if input_str in DialogueMappings.keys():
            if hasattr(self, DialogueMappings[input_str]):
                return getattr(self, DialogueMappings[input_str])()
        else:
            return self.confuse()

    def get_passport_responce(self):
        return DR.answ_ask_passport

    def get_start_date_responce(self):
        return DR.answ_ask_start_date

    def get_birth_date_responce(self):
        return DR.answ_ask_birthdate

    def get_end_date_responce(self):
        return DR.answ_ask_end_date

    def get_success_responce(self):
        return DR.answ_farewell

    def populate_person(self, input_str):
        if self.State == DialogueStates.Selling: #and len(input_str.split(" ")) == 3:
            self.Pers.fio = input_str
            self.State = DialogueStates.GettingPassport
        elif self.State == DialogueStates.GettingPassport: #and len(input_str) == 10:
            self.Pers.ser_num = input_str
            input_str = input_str.replace(" ", "")
            self.State = DialogueStates.GettingBirthDate
        elif self.State == DialogueStates.GettingBirthDate: #and len(input_str) == 10:
            self.Pers.day_of_birth = input_str
            self.State = DialogueStates.GettingStartDate
        elif self.State == DialogueStates.GettingStartDate: #and len(input_str.split(".")) == 3:
            self.Pers.start_of_tour = input_str
            self.State = DialogueStates.GettingEndDate
        elif self.State == DialogueStates.GettingEndDate: #and len(input_str.split(".")) == 3:
            self.Pers.finish_of_tour = input_str
            self.State = DialogueStates.Finish
        elif self.State == DialogueStates.GettingEndDate: #and len(input_str.split(".")) == 3:
            self.Pers.finish_of_tour = input_str
            self.State = DialogueStates.Finish
        elif self.State == DialogueStates.Finish:
            self.State = DialogueStates.Idle


    def confuse(self):
        if self.State != DialogueStates.Idle:
            return DR.answ_selling_error
        return DR.answ_unknown

    def reset_state(self):
        self.State = DialogueStates.Idle
        return DR.answ_cancel

    def show_help(self):
        return DR.answ_help

    def show_price(self):
        return DR.answ_price

    def say_hello(self):
        return DR.answ_hello

    def start_selling(self):
        self.State = DialogueStates.Selling
        return DR.answ_start_selling

    def ask_tour_start(self):
        return DR.answ_ask_start_date

    def ask_tour_stop(self):
        return DR.answ_ask_end_date

    def begin_payment(self):
        return DR.answ_ask_for_payment

    def say_bye(self):
        self.State = DialogueStates.Idle
        return DR.answ_bye

    def finish_procedures(self):
        self.State = DialogueStates.Idle
        return DR.answ_farewell

    def save(self):
        pass

    def load(self):
        pass

if __name__ == "__main__":
    help(DialogueHandler)