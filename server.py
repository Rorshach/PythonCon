from __future__ import division
import socket
import thread
import sys
import binascii
import numpy as np
from math import ceil

#Get host and port from file. Should be on azure
HOST = socket.gethostname()
PORT = 5050

print HOST, PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error code: ' + str(msg[0]) + 'Message: ' + str(msg[1])
    sys.exit()
s.listen(10)

# def creatMatrix(byteArray)

def getListOf16(lst):
    if len(lst) < 16:
        #Append empty elements to list and return list of size 16
        emptylstlen = 16 - len(lst)
        print emptylstlen
        emptyArr = np.zeros((emptylstlen, ), dtype = int)
        print emptyArr
        return np.reshape(np.append(lst, emptyArr), (4,4)) #may need to check dtype
    #TODO handle case when there are more than 16 elements
    numLists = ceil(len(lst)/16)
    print str(numLists) + "numlist"


def handleConnections(conn):
    conn.send("You are now connected to this server.\n")

    while True:
        #Receive 128 bits or 16 bytes from client (can be in hexa)
        data = conn.recv(1024) #buf size in bytes
        byteData = bytearray(data)
        # for b in byteData:
        #     print b
        #     print hex(b)

        arr = np.array(byteData)
        print arr
        arr16 = getListOf16(arr)
        print arr16
        print "Recieved: ", repr(data)
        if not data: break
        #convert to different message format (bytes)

    conn.close()

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr

    thread.start_new_thread( handleConnections, (conn, ))

s.close()
