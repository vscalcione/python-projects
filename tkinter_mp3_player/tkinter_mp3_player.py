from tkinter import * 

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

playlist_box = Listbox(root, bg="black", fg="green", width=60)
playlist_box.pack(pady=20)

root.mainloop()
