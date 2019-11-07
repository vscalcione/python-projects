## Text-editor developed by Scalcione Vincenzo ##
import tkinter as tk
from tkinter import *

import tkinter.filedialog as fd
from tkinter import *
from tkinter import messagebox, filedialog

class menuBar:
    def __init__ (self, parent):
        textFont = ('ubuntu', 12)
        menubar = tk.Menu(parent.master, font=textFont)
        parent.master.config(menu=menubar)
        fileDropdown = tk.Menu(menubar, font=textFont, tearoff=0)
        fileDropdown.add_command(label="New File", accelerator="Ctrl+N", command=parent.newFile)
        fileDropdown.add_command(label="Open File", accelerator="Ctrl+O", command=parent.openFile)
        fileDropdown.add_command(label="Save", accelerator="Ctrl+S", command=parent.save)
        fileDropdown.add_command(label="Save with name", accelerator="Ctrl+Shift+S", command=parent.saveAs)
        fileDropdown.add_separator()
        fileDropdown.add_command(label="Quit", command=parent.master.destroy)

        aboutDropdown = tk.Menu(menubar, font = textFont, tearoff=0)
        aboutDropdown.add_command(label="Release Notes", command=self.show_release_notes)
        aboutDropdown.add_separator()
        aboutDropdown.add_command(label="About", command=self.show_about_message)

        menubar.add_cascade(label="File", menu=fileDropdown)
        menubar.add_cascade(label="About", menu=aboutDropdown)


    def show_about_message(self):
        boxTitle = "About PyText"
        boxMessage = "Is a simple text editor made with Python and Tkinter library!"
        messagebox.showinfo(boxTitle, boxMessage)


    def show_release_notes(self):
        boxTitle = "Release Notes"
        boxMessage = "Version 0.1"
        messagebox.showinfo(boxTitle, boxMessage)


class statusBar:
    def __init__(self, parent):
        textFont = ('ubuntu', 12)
        self.status = tk.StringVar()
        self.status.set("PyText version 0.1")
        label = tk.Label(parent.textarea, textvariable=self.status, fg="black", bg="lightgrey", anchor='sw', font=textFont)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def updateStatus(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Your file is saved")
        else:
            self.status.set("PyText v 0.1")


class PyText:
    def __init__(self, master):
        master.title("New File (Untitled) - PyText")
        master.geometry("1200x700")
        textFont = ('ubuntu', 14)
        self.master = master
        self.filename = None
        self.textarea = tk.Text(master, font=textFont)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = menuBar(self)
        self.statusbar = statusBar(self)

        self.shortcutsBind()

    def setWindowTitle(self, name=None):
        if name:
            self.master.title(name + " - PyText")
        else:
            self.master.title("Untitled - PyText")

    def newFile(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.setWindowTitle()

    def openFile(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Batch  Executable files", "*.bat"),
                       ("Sh Linux files", ".sh"),
                       ("Python Script files", "*.py"),
                       ("Markdown Text files", "*.md"),
                       ("Javascript Script files", "*.js"),
                       ("HTML files", "*.html *.htm"),
                       ("Stylesheet files", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.setWindowTitle(self.filename)

    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.saveAs()

    def saveAs(self, *args):
        try:
            newFile = filedialog.asksaveasfilename(
                initialfile='.txt',
                defaultextension=".txt",
                filetypes=[("All files", "*.*"),
                           ("Text Files", "*.txt"),
                           ("Batch  Executable files", "*.bat"),
                           ("Sh Linux files", ".sh"),
                           ("Python Script files", "*.py"),
                           ("Markdown Text files", "*.md"),
                           ("Javascript Script files", "*.js"),
                           ("HTML files", "*.html *.htm"),
                           ("Stylesheet files", "*.css")])
            with open(newFile, 'w') as f:
                textarea_content = self.textarea.get(1.0, tk.END)
                f.write(textarea_content)
            self.filename = newFile
            self.setWindowTitle(self.filename)
            self.statusbar.updateStatus(True)
        except Exception as exception:
            print(exception)

    def shortcutsBind(self):
        self.textarea.bind('<Control-n>', self.newFile)
        self.textarea.bind('<Control-o>', self.openFile)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.saveAs)
        self.textarea.bind('<Key>', self.statusbar.updateStatus)

if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
