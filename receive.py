import socket
from Script import script

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20 # For fast response
ANSWER = "5 * 5 = " + str(script())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ("Connection address:", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("Received data:", data.decode())
    conn.send(ANSWER.encode())
conn.close()
