import socket
import json
def subscribe(): #Subscribe on Serafime
    sock = socket.socket()
    sock.connect(('api.seraphim.online', 20001))
    grt={"subscribe": True, "auth": "1b190253fc80765a897f0d39b13d1774dd34ee77de2116e62bc7121ab6fb625b", "opaque": 0}
    grt=json.dumps(grt)
    sock.send(grt.encode())

    data = sock.recv(1024)
    print (data)
    return(data)
subscribe()
