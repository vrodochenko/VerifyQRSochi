class Person:
    def __init__(self, fio, day_of_birth, ser_num, start_of_tour, finish_of_tour, id):
        self.fio = fio
        self.day_of_birth = day_of_birth
        self.ser_num = ser_num
        self.start_of_tour = start_of_tour
        self.finish_of_tour = finish_of_tour
        self.id = id
    def __init__(self):
        pass
    def restart(self):
        if len(self.__dict__) <6:
            return True
        else:
            return False

