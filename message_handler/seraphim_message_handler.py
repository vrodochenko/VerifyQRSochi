import socket
import json
sock = socket.socket()
sock.connect(('127.0.0.1', 9000))
grt={"subscribe": true, "auth": "1b190253fc80765a897f0d39b13d1774dd34ee77de2116e62bc7121ab6fb625b", "opaque": 0}
sock.send(grt.encode())
data = sock.recv(1024)
sock.close()
print (data.decode())
