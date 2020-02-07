import socket

host = '127.0.0.1'
port = 5005

host_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_connection.connect((host, port))
print("Connection established {}".format(port))

to_send = ""
while to_send != "end":
    to_send = input("> ")
    host_connection.send(to_send.encode())
    received = host_connection.recv(1024)
    print(received.decode())

print("Closing connection...")
host_connection.close()
print("Connection closed.")