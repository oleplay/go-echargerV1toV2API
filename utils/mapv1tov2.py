from operator import ge
from utils.request import getdata
def map():
    datav1 = getdata()
    datav2 = {}
    datav2['fwv'] = str(datav1['fwv'])
    datav2['car'] = int(datav1['car'])
    datav2['alw'] = bool(datav1['alw'])
    datav2['amp'] = int(datav1['amp'])
    # err
    datav2['err'] = int(datav1['err'])
    # eto
    datav2['eto'] = int(datav1['eto'])
    # psm
    # Phase Switching
    datav2['psm'] = int()
    # stp
    datav2['stp'] = int(datav1['stp'])
    # tmp
    datav2['tmp'] = int(datav1['tmp'])
    datav2['tma'] = int(datav1['tmp'])
    # trx
    datav2['trx'] = int(datav1['uby'])
    # nrg
    # datav1['nrg'] = datav1['nrg'].split(', ')
    print(datav1['nrg'])
    datav1['nrg'][11] = datav1['nrg'][11]*10
    datav1['nrg'][4] = datav1['nrg'][4]/10
    datav1['nrg'][5] = datav1['nrg'][5]/10
    datav1['nrg'][6] = datav1['nrg'][6]/10 
    datav2['nrg'] = datav1['nrg']
    # wh
    print(datav1['dws'])
    datav2['wh'] = float(datav1['dws'])/3600
    print(datav2['wh'])
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

    print (cards)
    datav2['cards'] = cards
    print(datav2)
    return datav2