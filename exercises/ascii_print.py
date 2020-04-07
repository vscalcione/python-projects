import tkinter as tk
import requests

# Questa funzione definisce il funzionamento del pulsante per il download della parola/frase inserita sotto forma di
# codice ASCII
window = tk.Tk()
window.geometry("800x700")
window.title("ASCII Art Generator")
window.grid_columnconfigure(0, weight=1)


def generate_ascii_code():
    if text_input.get():
        user_input = text_input.get()
        payload = {"text": user_input}
        response = requests.get("http://artii.herokuapp.com/make", params=payload)
        text_response = response.text
    else:
        text_response = "Add word or a phrase in input field"

    text_widget = tk.Text()
    text_widget.insert(tk.END, text_response)
    text_widget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)
    credits_label = tk.Label(window, text="Ascii Art ---> developed by: Scalcione Vincenzo")
    credits_label.grid(row=4, column=0, sticky="S", pady=10)


welcome_label = tk.Label(window, text="Welcome! Add word or a phrase in input field to be downloaded:", font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", padx=20, pady=10)
text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)
get_ascii_button = tk.Button(text="Generate ASCII Art", command=generate_ascii_code)
get_ascii_button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)

if __name__ == "__main__":
    window.mainloop()
