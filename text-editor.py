# ========== Text-editor developed by Scalcione Vincenzo ==========

import tkinter as tk

from tkinter import messagebox, filedialog


# =============================
# Definition of class MenuBar
# =============================

def show_about_messages():
    box_title = "About PyText"
    box_message = "Is a simple text editor made with Python and Tkinter library!"
    messagebox.showinfo(box_title, box_message)


class MenuBar:
    def __init__(self, parent):
        text_font = ('ubuntu', 12)
        menu_bar = tk.Menu(parent.master, font=text_font)
        parent.master.config(menu=menu_bar)
        file_dropdown = tk.Menu(menu_bar, font=text_font, tearoff=0)
        file_dropdown.add_command(label="New File", accelerator="Ctrl+N", command=parent.new_file)
        file_dropdown.add_command(label="Open File", accelerator="Ctrl+O", command=parent.open_file)
        file_dropdown.add_command(label="Save", accelerator="Ctrl+S", command=parent.save)
        file_dropdown.add_command(label="Save as", accelerator="Ctrl+Shift+S", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Quit", command=parent.master.destroy)

        about_dropdown = tk.Menu(menu_bar, font=text_font, tearoff=0)
        about_dropdown.add_command(label="Release Notes", command=self.show_release_notes)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="About", command=show_about_messages)

        info_dropdown = tk.Menu(menu_bar, font=text_font, tearoff=0)
        info_dropdown.add_command(label="Contact Me", command=self.show_personal_info)
        info_dropdown.add_separator()
        info_dropdown.add_command(label="About", command=self.show_personal_info)

        menu_bar.add_cascade(label="File", menu=file_dropdown)
        menu_bar.add_cascade(label="Info", menu=info_dropdown)
        menu_bar.add_cascade(label="About", menu=about_dropdown)

    @staticmethod
    def show_release_notes():
        box_title = "Release Notes"
        box_message = "Version 0.1"
        messagebox.showinfo(box_title, box_message)

    @staticmethod
    def show_personal_info():
        box_title = "Info"
        box_message = "Contact me with email at: vincenzo99.scalcione@gmail.com"
        messagebox.showinfo(box_title, box_message);


class StatusBar:
    def __init__(self, parent):
        text_font = ('ubuntu', 12)
        self.status = tk.StringVar()
        self.status.set("PyText version 0.1")
        label = tk.Label(parent.textarea, textvariable=self.status, fg="black", bg="lightgrey", anchor='sw', font=text_font)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Your file is saved")
        else:
            self.status.set("PyText v 0.1")


class PyText:
    def __init__(self, master):
        master.title("New File (Untitled) - PyText")
        master.geometry("1200x700")
        text_font = ('ubuntu', 14)
        self.master = master
        self.filename = None
        self.textarea = tk.Text(master, font=text_font)
        self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.menubar = MenuBar(self)
        self.statusbar = StatusBar(self)

        self.shortcuts_bind()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - PyText")
        else:
            self.master.title("Untitled file- PyText")

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Batch Executable files", "*.bat"),
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
            self.set_window_title(self.filename)

    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
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
            with open(new_file, 'w') as f:
                textarea_content = self.textarea.get(1.0, tk.END)
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as exception:
            print(exception)

    def shortcuts_bind(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()
