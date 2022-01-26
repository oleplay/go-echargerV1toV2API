from time import timezone
from urllib import request
import requests


def getdata():
    # get go-echarger data
    url = "http://go-eCharger/status"
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return r

def setdata(data):
    # set go-echarger data
    url = "http://go-eCharger/mqtt?payload="
    headers = {'Content-Type': 'application/json'}
    # Workaround weird query_params
    params = ""
    for i in data:
        # params += i + "=" + str(data[i])
        newurl = url + i + "=" + str(data[i])
        r = requests.post(newurl, headers=headers)
        # print(r.url)
        newurl = ""
    print (r.url)
    return r

def setdatafromv1(data):
    # set go-echarger data
    url = f"http://go-eCharger/mqtt?payload={data}"
    headers = {'Content-Type': 'application/json'}
    # Workaround weird query_params
    r = requests.post(url, headers=headers)
    # print(r.url)
    return r

def wait_for_boot():
    # wait for go-echarger to reboot
    url = "http://go-eCharger/status"
    headers = {'Content-Type': 'application/json'}
    while True:
        try:
            r = requests.get(url, headers=headers, timeout=1)
            # print(r.text)
            print(r.status_code)
            if r.status_code == 200 and r.json()['car'] == '4':
                return r
        except requests.exceptions.ConnectionError:
            print("Connection Error")
            pass