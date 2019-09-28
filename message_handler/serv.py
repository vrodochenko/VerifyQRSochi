import socket
import json
sock = socket.socket()
sock.bind(('127.0.0.1', 2001))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    if data.decode()=="Привет":
        conn.send("Здравствуйте. Для дальнейшей покупки введите Ваши ФИО полностью ".encode())
    else:
        conn.send("Повторите без ошибок".encode())
conn.close()
        

