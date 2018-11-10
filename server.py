import socket

#Get host and port from file. Should be on azure
HOST = ''
PORT = 5050
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1025) #buf size
    if not data: break
    #convert to different message format (bytes)
    message = "This is the message from the client."
    conn.sendall(message)

conn.close()