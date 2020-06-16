from tkinter import *

root = Tk()
root.title('Python Tkinter Paint')
root.geometry("800x800")

w = 600
h = 400

x1 = 0
x2 = 100
y1 = 300
y2 = 100

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

my_canvas.create_line(x1, y1, x2, y2, fill="red")

root.mainloop()

