import os
import telnetlib
import time

ip_eingabe = ""
port1 = -1
port2 = 50
start = 0

tn = telnetlib

ip_eingabe = input("Enter the IP address: ")
try:
    os.system("ping " + ip_eingabe) == 1
    print("Successfully!")
except:
    print("Bad!")
print("\b")
port1 = input("Enter the first port: ")
port1 = int(port1)
port2 = input("Enter the second port: ")
port2 = int(port2)


while port1 < port2:
    port1 += 1
    port_loop = format(port1)
    try:
        tn.Telnet(ip_eingabe,port_loop,1)
        print("[TCP-Port: " + format(port_loop) + "] Dieser Port ist Offen")
    except:
        print("[TCP-Port: " + format(port_loop) + "] Dieser Port ist nicht Offen")
    time.sleep(1)
