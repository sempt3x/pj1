import os
import telnetlib
from colorama import Fore

ip_eingabe = ""
port1 = -1
port2 = 50
start = 0

tn = telnetlib

ip_eingabe = input("Enter the IP address: ")
os.system("ping " + ip_eingabe) == 1
print("\b")
port1 = input("Enter the first port: ")
port1 = int(port1)
port2 = input("Enter the second port: ")
port2 = int(port2)
print("\n\n")

while port1 < port2:
    port1 += 1
    port_loop = format(port1)
    try:
        tn.Telnet(ip_eingabe, port_loop, 1)
        print(Fore.GREEN+"[TCP-Port: " + format(port_loop) + "] Port is open!")
    except:
        print(Fore.RED+"[TCP-Port: " + format(port_loop) + "] Port is not open!")
print(Fore.WHITE)