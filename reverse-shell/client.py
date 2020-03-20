import socket
import sys

def connect(address):
    """Stabilisci una connessione con address, quindi chiama receiver()"""
    try:
        s = socket.socket()
        s.connect(address)
        print("Connessione stabilita")
        print(f"Indirizzo : {address}")
    except socket.error as error:
        print("Qualcosa è andato storto... Info di seguito ")
        print(error)
        sys.exit()

if __name__ == "__main__":
    host = "192.168.233.1"
    port = 19876
    connect((host, port))

