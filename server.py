import socket
from Script import square, add_list, rem_list

host = ''
port = 5005

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(5)

connection, info = tcp_socket.accept()

received = connection.recv(1024)
script = b"None"
jeu = []
encheres = 0
while received != b"end":
    if encheres < 2:
        carte = connection.recv(1024)
        prise = carte.split(' ')
        if prise[0] == "reveal":
            prendre = input("Voulez-vous prendre ? (o/n) ")
            if prendre == "o":
                if encheres == 0:
                    message = "take 1"
                    connection.send(message.encode())
                if enchere == 1:
                    couleur = input("À quelle couleur voulez-vous prendre (nom entier à taper sans majuscule) : ")
                    message = "take 2 " + couleur
                    connection.send(message.encode())
            elif prendre == "n":
                message = "take no"
                connection.send(message.encode())
            encheres += 1
        elif prise[0] == "took":
            preneur = prise[1]
            atout = prise[2]
            encheres = 2
            break
   else:


print("Closing host...")
connection.close()
tcp_socket.close()
print("Host closed.")
