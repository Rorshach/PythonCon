import socket


message = ''
#Azure addr.
HOST = '168.62.192.26'
PORT = 5050
print HOST, PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error code: ' + str(msg[0] + 'Message: ' + msg[1])
    sys.exit()

while True:
    message = raw_input("What do you want to send the server? Enter: &*exit to quit.\n")
    if message == '&*exit':
        break
    byteMsg = bytearray(message)
    for b in byteMsg:
        print b

    s.send(byteMsg)
    data = s.recv(1024)
    print 'Received', repr(data)

s.close()
