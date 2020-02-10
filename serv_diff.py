import socket
from Script import square

host = ''
port = 5005

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(5)

connection, info = tcp_socket.accept()

received = connection.recv(1024)
script = b"None"
while received != b"end":
    if received.decode() == "script":
        connection.send("Which script do you want to use?\n1. Get the square of a number\n2. Move directory".encode())
        number = connection.recv(1024)
        b = int(number.decode())
        if b == 1:
            script = "Square"
        else:
            script = "Dir"
        
        if script == "Square":
            received = connection.recv(1024)
            a = int(received.decode())
            print(a)
            message = str(a) + " * " + str(a) + " = " + str(square(a))
            connection.send(message.encode())
            received = connection.recv(1024)
        elif script == "Dir":
            received = connection.recv(1024)
            message = "Directory = " + vm_dir(received.decode())
            connection.send(message.encode())
            received = connection.recv(1024)
    elif received.decode() == "end":
        break

print("Closing host...")
connection.close()
tcp_socket.close()
print("Host closed.")
