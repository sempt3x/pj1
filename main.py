import os
import telnetlib
from colorama import Fore

ip_eingabe = ''
port1 = 0
port2 = 50
start = 0
correct_counter = 0
fatal_counter = 0

tn = telnetlib

ip_eingabe = input("Enter the IP address: ")
os.system('ping ' + ip_eingabe) == 1
print('\b')
port1 = input('Enter the first TCP port: ')
port1 = int(port1)
port2 = input('Enter the second TCP port: ')
port2 = int(port2)
print("\n")
print(Fore.WHITE+'[SCAN] \n')
while port1 < port2:
    port1 += 1
    port_loop = format(port1)
    try:
        tn.Telnet(ip_eingabe, port_loop, 1)
        print(Fore.GREEN+'[TCP-Port: ' + format(port_loop) + '] Port is open!')
        correct_counter += 1
    except:
        print(Fore.RED+'[TCP-Port: ' + format(port_loop) + '] Port is not open!')
        fatal_counter += 1
print("\n")
print(Fore.WHITE+'[Status] \n')
print('Used IP: '+ip_eingabe)
print(Fore.GREEN+'Opened TCP Ports: '+format(correct_counter))
print(Fore.RED+'Closed TCP Ports: '+format(fatal_counter))
print(Fore.WHITE)