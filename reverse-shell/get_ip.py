import socket

def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Your hostname is: " + hostname)
    print("Your IP address is: " + ip_address)

if __name__ == "__main__":
    get_ip()