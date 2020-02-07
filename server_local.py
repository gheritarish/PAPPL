import socket
from Script import square

host = ''
port = 5005

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(5)

connection, info = tcp_socket.accept()

received = connection.recv(1024)
while received != b"end":
    a = int(received.decode())
    print(a)
    message = str(a) + " * " + str(a) + " = " + str(square(a))
    connection.send(message.encode())
    received = connection.recv(1024)

print("Closing host...")
connection.close()
tcp_socket.close()
print("Host closed.")
