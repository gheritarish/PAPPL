import socket

host = '10.0.2.4'
port = 5005

host_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_connection.connect((host, port))
print("Connection established on port: {}".format(port))

# La connection est effectuée, on peut envoyer notre nom puis la configuration de la partie
nom = input("Quel est votre nom ? ")
message = "name " + nom
connection.send(message.encode())
nb_hum = 4
while nb_hum > 3 or nb_hum < 0:
    nb_hum = int(input("Avec combien d'humains voulez-vous jouer ? (entre 0 et 3) "))
nb_ia = 3 - nb_hum
diff_ia = int(input("Quelle difficulté pour les IA ? (Valeur numérique, plus elle est élevée, plus les IA seront douées) "))
message = "against humans " + nb_hum + " ia " + nb_ia + " " + diff_ia
connection.send(message.encode())

# La configuration a été envoyée, on peut jouer
to_send = ""
jeu = []
encheres = 0

while received != b"end":
    ancien_pli = []
    pli = []
    if encheres < 2:
        carte = connection.recv(1024)
        carte = carte.decode()
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
       # On récupère l'ancien pli du serveur
       ancien = connection.recv(1024)
       ancien = ancien.decode()
       vieux_pli = ancien.split(' ')
       if vieux_pli[1] == 0:
           # Rien à afficher
       else:
            for i in range(1, 5):
                carte = vieux_pli[i].split('_')
                ancien_pli.append(carte)
            # On affiche l'ancien pli

        # On récupère le pli actuel du serveur
        actuel = connection.recv(1024)
        actuel = actuel.decode()
        pli_actuel = actuel.split(' ')
        if pli_actuel[1] == 0:
            # Rien à afficher au milieu
        else:
            for i in range(1, 5):
                carte = pli_actuel[i].split(' ')
                pli.append(carte)
            # On affiche le pli actuel au milieu

       jouer = # On récupère la carte qu'on veut jouer
       carte_a_jouer = str(jouer[0]) + '_' + str(jouer[1])
       message = "play " + carte_a_jouer
       connection.send(message.encode())
       if jouer[0] in ('Roi', 'Dame') and jouer[1] == atout:
           bel = input("Déclarer une belote ou rebelote ? (o/n) ")
           if bel == "o":
               print("1. Belote\n2. Rebelote")
               bel = int(input("Que déclarer ?"))
               if bel == 1:
                   message = "declare belote"
                   connection.send(message.encode())
               else:
                   message = "declare rebelote"
                   conneciton.send(message.encode())
            else:
                message = "declare none"
                connection.send(message.encode())


print("Closing host...")
connection.close()
tcp_socket.close()
print("Host closed.")
