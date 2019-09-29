import requests

fio = {"FIO": "Мамедов Игнат Эмильевич", "Day_of_birth": "28.08.1996", "Ser_num": "6342 445767",
       "Start_of_tour": "28.09.2019", "Finish_of_tour": "01.12.2019"}
res = requests.post('http://10.178.195.95:5000/value', json=fio)
if res.ok:
    print(res)
