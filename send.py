import socket

TCP_IP = '10.0.2.4'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = " Hello, World!\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Establish connection and send data
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE.encode())
    
    # Receive data
    data = s.recv(BUFFER_SIZE)

finally:
    s.close()


print ("received data:", data.decode())
