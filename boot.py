import machine
import network
import time
import  neopixel

np = neopixel.NeoPixel(machine.Pin(0), 16)



def do_connect(sta_if, station):
	
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.connect(station, 'VWMVXWXMQXVW36MN')
        return True
    else:
        return False



def gottacheckssids(sta_if):

    validssid = b'Odido-293C02'
    currentssids = sta_if.scan()
    currentssids = [x[0] for x in currentssids]
    if validssid in currentssids:
        return validssid 

    return None

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
lasttime = 0
tryconnect = True

while tryconnect: 
	if time.time() + 100 > lasttime:
		lasttime = time.time()+100
		connect = gottacheckssids(sta_if)

	if connect:
		tryconnect = do_connect(sta_if, connect)

print("reached end of programm")
