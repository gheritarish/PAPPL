# README
This script is made of four (4) different files. First, the `client.py` file, a script to connect a client to the server. Second, the `receive.py` file, a script to turn on the server and to track a message. This script has been improved into a server with the file `server.py`, which allows the user to open a server and send as many messages as they want. Finally, there is the `script.py`, which is a script to try to use the result of the function coming from another file.

## The `receive.py` script
This script opens the server and listen until a message is received. It prints on the screen the address of the sender (the address bound to the socket of the other end of the connection) then prints the message and sends to the original sender the result of `script.py`, which is 5 * 5 = 25. Finally, the server is closed.

## The `client.py` script
This script send a message to the IP address 10.0.2.4 (i.e. the original computer), port 5005. The server will ask the client to type a number. Then, the client types a number n and gets n * n. If the client types "end", the connection will be closed and the server will close as well.

## The `server.py` script
This script opens a server that will stay open until it receives a close message. This message is send when the client type "end". The `server.py` script uses the function `square` from the file `Script.py` to return n^2, where n is the number typed by the user.

## To run the script
On a terminal, run `python receive.py`, then open another terminal window to run `python client.py`. It will work with both `python2.7` and `python3` but the result will be better with `python3`. The file `receive.py` is not updated with the script and will return 5 * 5 = 25. 

To run the upgrade of this script, run `python server.py` then open another terminal and run `python client.py`. Be careful with the IP addresses: this script has been written between a Linux virtual machine (the user) and the original OS (the server), hence sending a message to `10.0.2.4`.

### Sources
https://docs.python.org/2/library/socket.html

https://www.techbeamers.com/python-tutorial-write-tcp-server/

https://wiki.python.org/moin/TcpCommunication

https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/234698-gerez-les-reseaux
