import requests
res = requests.post('http://localhost:5000/value', json={"mytext":"lalala"})
if res.ok:
    print(res)
