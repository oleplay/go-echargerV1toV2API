from concurrent.futures import thread
import imp
from webbrowser import get
from utils import getdata, setdata, wait_for_boot
import threading


# Get Data --> Persist Current --> Disallow Charging --> wait until not charging --> Switch phases --> wait until booted --> set previous Current --> Allow Charging

def start_switching():
    finished = threading.Event()
    thread = threading.Thread(target=switch_phases, args=(finished,))
    thread.start()
    finished.wait()
    return getdata().json()

def switch_phases(finished):
    # Get data
    data = getdata().json()
    # print(data)
    # Persist current
    amp = data["amp"]
    # print(amp)
    # Disallow charging
    setdata({'alw': 0})
    print(data['pha'])
    # Wait until not charging
    while (data['car'] == 4) and (data['nrg'][4] == 0) and ((data['pha'] == 56) or (data['pha'] == 8)):
        print("Waiting for car to stop charging")
        data = getdata().json()

    print("Car stopped charging" + str(data['pha'] + data['car']))
    # Switch phases
    ## Call Tasmota Switch

    # Wait until booted
    data = wait_for_boot()


    while data.status_code != 200 and data.json()['car'] != 4:
        data = getdata()

    
    # Set previous current
    setdata({'amp': amp})
    # Allow charging
    setdata({'alw': 1})
    finished.set()
    return data
