import socketserver

class Handler_TCPServer(socketserver.BaseRequestHandler):
    """The TCP Server class"""

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(format(self.client_address[0]))
        print(self.data)

        answer = "5 * 5 = " + script()
        self.request.sendall(answer.encode())

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5005

    # Init the TCP server object
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)

    tcp_server.serve_forever() # Need to press Ctrl-C to stop
