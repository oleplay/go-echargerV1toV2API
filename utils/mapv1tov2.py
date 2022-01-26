from operator import ge
from utils.request import getdata
def map_read():
    r = getdata()
    datav1 = r.json()
    datav2 = {}
    datav2['fwv'] = str(datav1['fwv'])
    datav2['car'] = int(datav1['car'])
    datav2['alw'] = bool(int(datav1['alw']) == 1)
    # print('Test' + str(datav2['alw']))
    datav2['amp'] = int(datav1['amp'])
    # err
    datav2['err'] = int(datav1['err'])
    # eto
    datav2['eto'] = int(datav1['eto'])
    # psm
    # Phase Switching
    # Detect 3 phase or single phase
    # 56 --> 111000 --> 3 phase
    # 63 --> 111111 --> 3 phase

    # EVCC 3 phase detection done via 'nrg' current values

    if datav1['pha'] == '56' or datav1['pha'] == '63':
        datav2['psm'] = '2'
    else:
        datav2['psm'] = '1'
    # datav2['psm'] = 
    # stp
    datav2['stp'] = int(datav1['stp'])
    # tmp
    datav2['tmp'] = int(datav1['tmp'])
    datav2['tma'] = int(datav1['tmp'])
    # trx
    datav2['trx'] = int(datav1['uby'])
    # nrg
    # datav1['nrg'] = datav1['nrg'].split(', ')
    # print(datav1['nrg'])
    datav1['nrg'][11] = datav1['nrg'][11]*10
    datav1['nrg'][4] = datav1['nrg'][4]/10
    datav1['nrg'][5] = datav1['nrg'][5]/10
    datav1['nrg'][6] = datav1['nrg'][6]/10
    
    # 3 Phase testing 
    # datav1['nrg'][5] = datav1['nrg'][4]
    # datav1['nrg'][6] = datav1['nrg'][4]

    datav2['nrg'] = datav1['nrg']
    # wh
    # print(datav1['dws'])
    datav2['wh'] = float(datav1['dws'])/360
    # print(datav2['wh'])
    # cards
    cards = ({"name": datav1['rna'], "energy": float(datav1['eca']), "CardID": bool(datav1['rca'])},
        {"name": datav1['rnm'], "energy": float(datav1['ecr']), "CardID": bool(datav1['rcr'])},
        {"name": datav1['rne'], "energy": float(datav1['ecd']), "CardID": bool(datav1['rcd'])},
        {"name": datav1['rn4'], "energy": float(datav1['ec4']), "CardID": bool(datav1['rc4'])},
        {"name": datav1['rn5'], "energy": float(datav1['ec5']), "CardID": bool(datav1['rc5'])},
        {"name": datav1['rn6'], "energy": float(datav1['ec6']), "CardID": bool(datav1['rc6'])},
        {"name": datav1['rn7'], "energy": float(datav1['ec7']), "CardID": bool(datav1['rc7'])},
        {"name": datav1['rn8'], "energy": float(datav1['ec8']), "CardID": bool(datav1['rc8'])},
        {"name": datav1['rn9'], "energy": float(datav1['ec9']), "CardID": bool(datav1['rc9'])},
        {"name": datav1['rn1'], "energy": float(datav1['ec1']), "CardID": bool(datav1['rc1'])})

    # print (cards)
    datav2['cards'] = cards

    # frc
    if datav1['alw'] == '1':
        datav2['frc'] = 2
    elif datav1['alw'] == '0':
        datav2['frc'] = 1
    # print(datav2)
    return datav2, r

def map_set(set_data):
    datav1 = {}
    modified_data = {}
    # print(set_data)
    if 'dwo' in set_data:
        set_data['dwo'] = int(set_data['dwo']/1000)
    if 'amp' in set_data:
        set_data.update({'amx': int(set_data['amp'])})
        set_data.pop('amp')
    if 'alw' in set_data:
        set_data['alw'] = int(bool(str(set_data['alw']).capitalize() == 'True'))
    # Change in allow charge parameter 0--> ignore 1--> disallow 2--> allow
    if 'frc' in set_data:
        set_data['frc'] = int(set_data['frc'])
        if set_data['frc'] == 2:
            set_data['frc'] = 1
        elif set_data['frc'] == 1:
            set_data['frc'] = 0
        elif set_data['frc'] == 0:
            curr_data = getdata().json()
            # print('Ignore' + str(curr_data['alw']))
            set_data['frc'] = int(curr_data['alw'] == True)
            
        # print(set_data['frc'])
        set_data.update({'alw': set_data['frc']})
        set_data.pop('frc')
    for i in set_data:
        datav1.update({i : set_data[i]})
    # print(datav1)
    return datav1
    print(datav1)

