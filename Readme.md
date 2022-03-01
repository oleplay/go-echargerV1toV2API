# go-eCharger V2 to V1 API
The aim of this Project is to provide a translation layer for the new go-eCharger V2 API to enable phase switching for an V2 Wallbox with evcc and an external switching device.

Because i don't own an V3 Wallbox all information was obtained from the evcc source code or the offical API docs from go-e.

## conversion from V2 to V1 and back
only parameters needed for evcc control listed.



### V1 --> V2 read from wallbox
| V1 param | V1 datatype | V2 param | V2 datatype |  conversion V1 --> V2 |
|-|-|-|-|-|
| alw (allow charging) | int | alw | bool | 1 = True |
| nrg (voltage & current) | array | nrg | array | total power * 10 <br> ampereL1,2,3 /10 </br>|
| dws (loaded energy) | int | wh | double | dws/360 |
| rna...rn1 (rfid name)<br> eca...ec1 (rfid energy) <br> rca...rc1 (rfid id)</br> | rc = string <br> rn = string <br> ec = int | cards | array | cards[0] = {"name" : rna, "energy" : float(eca), "CardID" : bool(rca)} <br> cards[1] = {"name" : rnm, "energy" : float(ecr), "CardID" : bool(rcr)} <br> ... </br>|
| alw (allow charging) | int | frc (force state) | int | alw 1 = frc 2 <br> alw 0 = frc 1 </br>
| pha (phase ) | (binary as int) <br> int | pha <br> psm (phase detection & switching) | int <br> int | pha = pha <br> pha 56 = psm 2 <br> pha 63 = psm 1


No conversion needed:

| V1 param | V2 param |
|-|-|
| fwv (firmware version) | fwv |
| car (car status) | car |
| amp (current) | amp |
| err (error) | err |
| eto (energy total) | eto |
| stp (stop state) | stp |
| tmp (controller temp) | tmp <br> tma |
| uby (unlocked by) | trx (transaction) |

### V2 --> V1 write to wallbox
| V2 param | V2 datatype | V1 param | v1 datatype | conversion V2 --> V1
|-|-|-|-|-|
| dwo (energy limit) | double | dwo | int | dwo/1000 |
| amp (current) | int | amx (current not saved) | int | amp = amx |
| alw (allow charging) | bool | alw | int | True = 1 |
| frc (force state) | int | alw | int | frc 2 = alw 1 <br> 1 = 0 <br> 0 = current alw / ignore </br> |

