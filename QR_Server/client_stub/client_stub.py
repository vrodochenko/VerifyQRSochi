import requests
fio = {"FIO":"Арабаджиян Артем Лукьянович", "Day_of_birth":"29.12.2012", "Ser_num":"6012 566778", "Start_of_tour":"12.12.2016", "Finish_of_tour":"31.12.2016"}
res = requests.post('http://10.178.195.95:5000/value', json=fio)
if res.ok:
    print(res)
