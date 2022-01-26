import requests

def getdata():
    # get go-echarger data
    url = "http://go-eCharger/status"
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    x = dict(r.json())
    return x

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
        print(r.url)
        newurl = ""
    print (r.url)
    return r