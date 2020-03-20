import socket
import sys

def server(address):
    """Inizializza un server socket e attendi una connession"""
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Inizializzato. Sono in ascolto...")
    except Exception as e:
        print("\nSembra che qualcosa sia andato storto. ")
        print(e)
        restart = input("\nVuoi che reinizializzi il server? s/n ")
        if restart.lower() == "s" or restart.lower() == "si":
            print("\nRicevuto. Sto reinizializzando il server... \n")
            server(address)
        else:
            print("\nA presto, ed Happy Coding! ;) \n")
            sys.exit()
    conn, client_addr = s.accept()
    print(f"Connessione stabilita: {client_addr} ")

if __name__ == "__main__":
    host = "192.168.233.1"
    port = 19876
    server((host, port))

