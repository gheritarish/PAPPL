# README
This script is made of four (4) different files. First, the `client.py` file, a script to connect a client to the server. Second, the `receive.py` file, a script to turn on the server and to track a message. This script has been improved into a server with the file `server.py`, which allows the user to open a server and send as many messages as they want. Finally, there is the `script.py`, which is a script to try to use the result of the function coming from another file.

## The `client.py` script
This script send a message to the IP address 10.0.2.4 (i.e. the original computer), port 5005. The server will ask the client whether they want to use a script or end the connection. If the client chooses to use a script, they will then have to choose between script 1 (computing the square of a number) or script 2 (playing with a list stored on the server). In the first case, the client types a number n and gets n * n. In the second case, the client will have to choose either 1 to add numbers to the list, or 2 to remove a specific number from it.

If the client types "end", the connection will be closed and the server will close as well.

## The `server.py` script
This script opens a server that will stay open until it receives a close message. This message is send when the client type "end". The `server.py` script uses the function `square` from the file `Script.py` to return n^2, where n is the number typed by the user. It also uses the `add_list` and `rem_list` functions to respectively add a number ot a list or remove one from it.

## To run the script
On a terminal, run `python server.py`, then open another terminal window to run `python client.py`. It will work with both `python2.7` and `python3` but the result will be better with `python3`. Be careful with the IP addresses: this script has been written between a Linux virtual machine (the user) and the original OS (the server), hence sending a message to `10.0.2.4`.

### Sources
https://docs.python.org/2/library/socket.html

https://www.techbeamers.com/python-tutorial-write-tcp-server/

https://wiki.python.org/moin/TcpCommunication

https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234698-gerez-les-reseaux
