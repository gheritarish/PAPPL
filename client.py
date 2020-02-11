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
        print(received.decode())
        number_to_send = input("> ")
        host_connection.send(number_to_send.encode())
        if int(number_to_send) == 1:
            to_send = input("Enter n to get n*n or 'end' to close the connection:\n> ")
            host_connection.send(to_send.encode())
            received = host_connection.recv(1024)
            print(received.decode())
        elif int(number_to_send) == 2:
            current = host_connection.recv(1024)
            print(current.decode())
            
            num = input("Do you want to:\n1. Add elements to the list\n2. Remove an element from the list\n> ")
            host_connection.send(num.encode())
            
            if int(num) == 1:
                to_send = input("Write down the length of the list:\n> ")
                host_connection.send(to_send.encode())
                for i in range(int(to_send)):
                    next_number = input("Next number of the list\n> ")
                    host_connection.send(next_number.encode())
            elif int(num) == 2:
                to_send = input("Write down the number you want to remove\n> ")
                host_connection.send(to_send.encode())
            else:
                break

            received = host_connection.recv(1024)
            print(received.decode())
        

print("Closing connection...")
host_connection.close()
print("Connection closed.")
