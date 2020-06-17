from tkinter import *

root = Tk()
root.title('Python Tkinter Paint')
root.geometry("800x800")

w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

my_canvas.create_line(0, 100, 300, 100, fill="red")
my_canvas.create_line(150, 0, 150, 200, fill="red")

root.mainloop()

