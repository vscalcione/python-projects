import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger

from main_gui import GUI

""" Bergue Remote Access Tool
Description:
- It is a RAT used for control PCs
- Main Python file, used for starting all others

"""


def main():
    # Create a main TK object
    root = tk.Tk()

    # Remove for just askstring appear
    root.withdraw()

    # Void variables for while loops
    address = ''
    port = 0

    # Get address and port
    # While loop to user do not click in cancel
    while not address:
        address = askstring('Address', 'Host Address: ')

    # While loop to user do not click in cancel
    while not port:
        port = askinteger('Port', 'Port number:')

    # Start GUI class
    GUI(root, address, port).pack(side="top", fill="both", expand=True)

    # Enter in mainloop
    root.mainloop()


if __name__ == "__main__":
    main()
