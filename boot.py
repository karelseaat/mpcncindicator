import time
import network
import socket
import machine, neopixel


def display_state(state, np):
    print(state)
    
    if state == "Idle":
        np.fill((255,255,0))
    elif state == "Alarm":
        np.fill((255,0,0))
    elif state == "Run":
        np.fill((0,255,0))
    else:
        np.fill((0,0,0))

    np.write()


np = neopixel.NeoPixel(machine.Pin(10), 16)

np.fill((100,100,100))
np.write()
station = network.WLAN(network.STA_IF)
station.active(True)
station.disconnect()
# Network settings
wifi_ssid = "Odido-293C02"
wifi_password = "VWMVXWXMQXVW36MN"
print("Scanning for WiFi networks, please wait...")
authmodes = ['Open', 'WEP', 'WPA-PSK' 'WPA2-PSK4', 'WPA/WPA2-PSK']
for (ssid, bssid, channel, RSSI, authmode, hidden) in station.scan():
  print("* {:s}".format(ssid))
  print("   - Channel: {}".format(channel))
  print("   - RSSI: {}".format(RSSI))
  print("   - BSSID: {:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}".format(*bssid))
  print()

# Continually try to connect to WiFi access point
while not station.isconnected():
    # Try to connect to WiFi access point
    print("Connecting...")
    station.connect(wifi_ssid, wifi_password)
    time.sleep(10)

np.fill((100,0,100))
np.write()
print("done connecting to wifi!!")
resolved = False

while not resolved:
    try:
        addr_info = socket.getaddrinfo("munchy.local", 23)
        addr = addr_info[0][-1]
        resolved = True
    except:
        print("not resolved")

np.fill((0,100,100))
np.write()

s = socket.socket()
s.connect(addr)
s.settimeout(10)

print("addr:", addr)

while True:
    time.sleep(2)
    print("sending status question.")
    s.send("?\n")
    try:
        data = s.recv(500)
        display_state(str(data, 'utf8').split("|")[0][1:], np)
    except Exception as e:
        print("stuff whent wrong!", e)

