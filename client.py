import socket

host = '10.0.2.4'
port = 5005

host_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_connection.connect((host, port))
print("Connection established on port: {}".format(port))

to_send = ""
while to_send != "end":
    to_send = input("Type 'end' to close the connection, 'script' to continue\n> ")
    host_connection.send(to_send.encode())
    received = host_connection.recv(1024)
    
    if to_send == "script":
        number_to_send = input("Which script do you want to use?\n1. Get the square of a number\n2. Move directory\n> ")
        host_connection.send(number_to_send.encode())
        if int(number_to_send) == 1:
            to_send = input("Enter n to get n*n or 'end' to close the connection:\n> ")
            host_connection.send(to_send.encode())
            received = host_connection.recv(1024)
            print(received.decode())
        elif int(number_to_send) == 2:
            to_send = input("Type the name of a directory")
            host_connection.send(to_send.encode())
            received = host_connection.recv(1024)
            print(received.decode())
        

print("Closing connection...")
host_connection.close()
print("Connection closed.")
