import socket

host = ''
port = 5005

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(5)

connection, info = tcp_socket.accept()

# La connection est effectuée
received = connection.recv(1024)
message = received.decode()
nom = message.split(' ')
name = nom[1]
received = connection.recv(1024)
message = received.decode()
config = message.split(' ')
nb_hum = config[2]
nb_ia = config[4]
if nb_ia != 0:
    diff_ia = config[5]
else:
    diff_ia = 0

jeu = []
encheres = 0
received = ""
# Tirage de cartes
atout = # Carte révélée
pli = []
ancien_pli = []
while received != "end":
    if encheres < 2:
        message = "reveal " + atout[0] + '_' + atout[1]
        connection.send(message.encode())
        # Puis on reçoit la réponse du client
        received = connection.recv(1024)
        message = received.decode()
        prise = message.split(' ')
        if prise[1] == 1:
            message = "took joueur " + atout[1]
            connection.send(message.encode())
        elif prise[1] == 2:
            message = "took joueur " + prise[2]
            connection.send(message.encode())
        else:
            break
    else:
        # On envoie d'abord les cartes de l'ancien pli
        if ancien_pli == []:
            message = "pli 0"
        else:
            cartes_pli = ""
            for carte in ancien_pli:
                cartes_pli.append(carte[0] + '_' + carte[1] + ' ')
            message = "pli " + cartes_pli
            connection.send(message.encode())
        # On envoie ensuite celles du nouveau pli
        if pli == []:
            message = "actual 0"
        else:
            cartes_pli = ""
            for carte in pli:
                cartes_pli.append(carte[0] + '_' + carte[1] + ' ')
            message = "pli " + cartes_pli
            connection.send(message.encode())
        
        # Puis on récupère la carte jouée par le joueur
        received = connection.recv(1024)
        received = received.decode()
        joue = received.split(' ')
        carte = joue[1].split('_')
        pli.append(carte)
        if pli.length() == 4:
            # On commence par gérer la victoire du pli

            # Puis on fait un transfert dans les listes
            ancien_pli = pli
            pli = []
