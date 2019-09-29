import sqlite3
import json


class TicketDAO(object):

    def __init__(self):
        pass

    def search(self,param, search_param): #param - то по какому стобцу ищем, search_param - то что ищем(id)
        conn = sqlite3.connect('sqlite_tick.db')
        cursor = conn.cursor()
        if param=="fio":
            cursor.executemany("SELECT * FROM Tickets where fio=?",search_param)
            results = cursor.fetchall()
        elif param=="id":
            cursor.execute("SELECT * FROM Tickets where id=?", search_param)
            results = cursor.fetchall()
        elif param=="serNum":
            cursor.executemany("SELECT * FROM Tickets where serNum=?", search_param)
            results = cursor.fetchall()
        elif param=="finishOfTour":
            cursor.executemany("SELECT * FROM Tickets where finishOfTour=?", search_param)
            results = cursor.fetchall()
        elif param=="startOfTour":
            cursor.executemany("SELECT * FROM Tickets where startOfTour=?", search_param)
            results = cursor.fetchall()
        elif param=="dayOfBirth":
            cursor.executemany("SELECT * FROM Tickets where dayOfBirthr=?", search_param)
            results = cursor.fetchall()
        print(results)
        conn.close()
        return(results)
    
    def add(self):
        conn = sqlite3.connect('sqlite_tick.db')
        cursor = conn.cursor()
        id=1
        fio="Test"
        serNum="test"
        finishOfTour="21.01.1992"
        startOfTour="21.12.1991"
        dayOfBirth="21.01.1990"
        b=[id,fio,serNum, finishOfTour, startOfTour, dayOfBirth]
        cursor.executemany("INSERT INTO Tickets VALUES (?,?,?,?,?,?)",b)
        conn.commit()
        results = cursor.fetchall()
        conn.close()
        return(results)

    def check(self):
        conn = sqlite3.connect('sqlite_tick.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Tickets ")
        results = cursor.fetchall()
        print(results[0])
        conn.close()
        return (results)

ti1=TicketDAO()
ti1.search("id",'1')
ti1.check()

