import Tkinter as tk
window = tk.Tk()
window.geometry("600x600")
window.title("Python Interface with TkInter")
window.resizable(False, False)
window.configure(background="cyan")


# This function define a label for the interface and a button functionalityf
def first_function():
    text = "Hello World"
    text_output = tk.Label(window, text=text, fg="red", font=("Segoe UI", 16))
    text_output.grid(row=0, column=1, sticky="W")


def second_function():
    text = " New message, New function !"
    text_output = tk.Label(window, text=text, fg="green", font=("Segoe UI", 16))
    text_output.grid(row=1, column=1, padx=50, sticky="W")


first_button = tk.Button(text="Say Hello!", command=first_function)
first_button.grid(row=0, column=0, sticky="W")
second_button = tk.Button(text="2nd Function", command=second_function)
second_button.grid(row=1, column=0, pady=20, sticky="W")


if __name__ == "__main__":
    window.mainloop()
