import socket

host = ''
port = 5005

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(5)

connection, info = tcp_socket.accept()

received = b""
while received.decode() != "end":
    received = connection.recv(1024)
    print(received.decode())
    connection.send("Message received".encode())

print("Closing host...")
connection.close()
tcp_socket.close()
print("Host closed.")