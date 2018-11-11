import socket
import thread

#Get host and port from file. Should be on azure
HOST = socket.gethostname()
PORT = 5050

print HOST, PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error code: ' + str(msg[0] + 'Message: ' + msg[1])
    sys.exit()
s.listen(10)

def handleConnections(conn):
    conn.send("You are now connected to this server.\n")

    while True:

        #Receive 128 bits or 16 bytes from client (can be in hexa)
        data = conn.recv(1024) #buf size in bytes
        print "Recieved: ", repr(data)
        if not data: break
        #convert to different message format (bytes)

    conn.close()

while 1:
    conn, addr = s.accept()
    print 'Connected by', addr

    thread.start_new_thread( handleConnections, (conn, ))

s.close()
