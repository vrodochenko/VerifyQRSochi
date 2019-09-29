import sqlite3
import json


class BlackListDAO(object):

    def __init__(self):
        pass

    def search(self): #search with id
        conn = sqlite3.connect('sqlite.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ban_list where id=?",str(2))
        results = cursor.fetchall()
        print(results)
        conn.close()
        return(results)
    
    def add(self):
        conn = sqlite3.connect('sqlite.db')
        cursor = conn.cursor()
        b=[[2,"asdasd"]]
        cursor.executemany("INSERT INTO ban_list VALUES (?,?)",b)
        conn.commit()
        results = cursor.fetchall()
        print(len(results))
        conn.close()
        return(results)

    def check(self):
        conn = sqlite3.connect('sqlite.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ban_list ")
        results = cursor.fetchall()
        print(results)
        conn.close()
        return (results)


