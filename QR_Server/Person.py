import json

class Person:
    def __init__(self):
        self.fio = None
        self.day_of_birth = None
        self.ser_num = None
        self.start_of_tour = None
        self.finish_of_tour = None
        self.id = "000"

    def serialize(self):
        return json.dumps(self.__dict__)

    def serialize_to_iphone(self):
        # {"id":"736492749sduyakszsv",
        # "FIO":"ванов Иван Иванович",
        # "Day_of_birth":"01.10.1993",
        # "Ser_num":"29.10.1993",
        # "Start_of_tour":"01.10.1993",
        # "Finish_of_tour":"01.10.1994"}

        iphone_dict = {
            "id": self.id,
            "FIO": self.fio,
            "Day_of_birth": self.day_of_birth,
            "Ser_num": self.id,
            "Start_of_tour": self.start_of_tour,
            "Finish_of_tour": self.finish_of_tour
        }
        return json.dumps(iphone_dict)


if __name__ == "__main__":
    a = Person()
    a.fio = "Hi"
    a.day_of_birth = "Hi"
    a.ser_num = "Hi"
    a.start_of_tour = "Hi"
    a.finish_of_tour = "Hi"
    a.id = "ho"
    print(a.__dict__)
    print(a.serialize())