from tkinter import * 
from PIL import ImageTk, Image

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

# Create Playlist Box
playlist_box = Listbox(root, bg="black", fg="green", width=60)
playlist_box.pack(pady=20)

# Define Button Images
back_btn_image = ImageTk.PhotoImage(Image.open('images/back.png'))
play_btn_image = ImageTk.PhotoImage(Image.open('images/play.png'))
pause_btn_image = ImageTk.PhotoImage(Image.open('images/pause.png'))
stop_btn_image = ImageTk.PhotoImage(Image.open('images/stop.png'))
forward_btn_image = ImageTk.PhotoImage(Image.open('images/forward.png'))

# Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20) 

# Create Buttons (Play/Stop/Next Track/Previous Track/Pause)
back_button = Button(control_frame, text="Back", image=back_btn_image)
play_button = Button(control_frame, text="Play", image=play_btn_image)
pause_button = Button(control_frame, text="Pause", image=pause_btn_image)
stop_button = Button(control_frame, text="Stop", image=stop_btn_image)
forward_button = Button(control_frame, text="Forward", image=forward_btn_image)

back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
forward_button.grid(row=0, column=4, padx=10)


root.mainloop()
