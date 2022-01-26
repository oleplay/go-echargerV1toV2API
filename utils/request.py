
import requests

def getdata():
    # get go-echarger data
    url = "http://go-eCharger/status"
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    x = dict(r.json())
    return x