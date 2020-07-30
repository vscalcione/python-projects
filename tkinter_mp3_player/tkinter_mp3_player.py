from tkinter import * 
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

# Create function to add one song to the playlist
def add_song():
	song = filedialog.askopenfilename(initialdir='audio/', title='Choose a song', filetypes=(('mp3 Files', '*.mp3'),)) 	
	my_label.config(text=song)

# Create function to add many songs to the playlist
def add_many_songs():
	pass

# Create Playlist Box
playlist_box = Listbox(root, bg="black", fg="green", width=60)
playlist_box.pack(pady=20)

# Define Button Images
back_btn_image = ImageTk.PhotoImage(Image.open('images/back.png'))
pause_btn_image = ImageTk.PhotoImage(Image.open('images/pause.png'))
play_btn_image = ImageTk.PhotoImage(Image.open('images/play.png'))
stop_btn_image = ImageTk.PhotoImage(Image.open('images/stop.png'))
forward_btn_image = ImageTk.PhotoImage(Image.open('images/forward.png'))

# Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20) 

# Create Buttons (Play/Stop/Next Track/Previous Track/Pause)
back_button = Button(control_frame, text="Back", image=back_btn_image, borderwidth=0)
pause_button = Button(control_frame, text="Pause", image=pause_btn_image, borderwidth=0)
play_button = Button(control_frame, text="Play", image=play_btn_image, borderwidth=0)
stop_button = Button(control_frame, text="Stop", image=stop_btn_image, borderwidth=0)
forward_button = Button(control_frame, text="Forward", image=forward_btn_image, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
forward_button.grid(row=0, column=4, padx=10)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdown
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)

# Add one song to playlist
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)

# Add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)

# Add temporary label
my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()
