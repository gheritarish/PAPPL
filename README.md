# README
This script uses two (2) different files. First, the `send.py` file, a script to send a message to the server. Second, the `receive.py` file, a script to turn on the server and to track a message.

## The `send.py` script
This script send a message to the IP address 127.0.0.1 (i.e. the `localhost`), port 5005. The script then sends a "Hello, World!" message to the server. The server sends back a message that we will print on the sceen after closing the connection.

## The `receive.py` script
This script opens the server and listen until a message is received. It prints on the screen the address of the sender (the address bound to the socket of the other end of the connection) then prints the message and sends it back to the original sender. Finally, the server is closed.

## To run the script
On a terminal, run `python receive.py`, then open another terminal window to run `python send.py`. It will work with both `python2.7` and `python3` but the result will be better with `python3`.
