# README
This script is made of four (4) different files. First, the `send.py` file, a script to send a message to the server. Second, the `receive.py` file, a script to turn on the server and to track a message. This script has been improved into a server with the file `server.py`, which allows the user to open a server and send as many messages as they want. Finally, there is the `script.py`, which is a script to try to use the result of the function coming from another file.

## The `send.py` script
This script send a message to the IP address 127.0.0.1 (i.e. the `localhost`), port 5005. The script then sends a "Hello, World!" message to the server. The server sends back a message that we will print on the sceen after closing the connection.

## The `receive.py` script
This script opens the server and listen until a message is received. It prints on the screen the address of the sender (the address bound to the socket of the other end of the connection) then prints the message and sends to the original sender the result of `script.py`, which is 5 * 5 = 25. Finally, the server is closed.

## The `server.py` script
This script creates a server that will definitely stay open. As long as it is opened, we can send as many messages as we want to the server. The answer will always be the same, since it's a try to know if it works.

## To run the script
On a terminal, run `python receive.py`, then open another terminal window to run `python send.py`. It will work with both `python2.7` and `python3` but the result will be better with `python3`.

To run the upgrade of this script, run `python server.py` then open another terminal and run `python send.py`. Be careful with the IP addresses: this script has been written between a Linux virtual machine (the user) and the original OS (the server), hence sending a message to `10.0.2.4`.

### Sources
https://docs.python.org/2/library/socket.html
https://www.techbeamers.com/python-tutorial-write-tcp-server/
https://wiki.python.org/moin/TcpCommunication
