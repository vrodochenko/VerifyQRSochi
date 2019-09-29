import sqlite3

con = sqlite3.connect('users.db')


class SqlTable:
    def __init__(self, con):
        self.con = con

    def __init__(self):
        self.con = sqlite3.connect('users.db')

    def upload(self, pes_hash):
        try:
            cur = con.cursor()
            ask_test = "INSERT INTO users (hash) VALUES(" + '"' + pes_hash + '"' + ")"
            cur.execute(ask_test)
            con.commit()
            print(cur.lastrowid)
            return 0
        except:
            return 1

    def read_from(self, pes_hash):
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE hash = " + '"' + pes_hash + '"')
        if len(cur.fetchall()) > 0:
            return True
        else:
            return False
        con.close()
