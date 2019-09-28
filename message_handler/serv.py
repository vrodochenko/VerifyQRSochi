import socket
import json
sock = socket.socket()
sock.bind(('127.0.0.1', 9000))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    if not data:
        break
    if data.decode()=="Привет":
        conn.send("Salam vualeykum. Che biletu zahotel? Lan u menya norm nastroy. Pishu svoi dannue, pes".encode())
    else:
        conn.send("Ne po sezonu shelestish".encode())
conn.close()
        

