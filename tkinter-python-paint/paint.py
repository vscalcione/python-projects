from tkinter import *

root = Tk()
root.title('Python Tkinter Paint')
root.geometry("800x800")

def paint(event):

	# Starting position
	x1 = event.x - 1
	y1 = event.y - 1

	# Ending position
	x2 = event.x + 1
	y2 = event.y + 1

	# Draw on the canvas
	my_canvas.create_line(x1, y1, x2, y2, fill="red", smooth=True)

w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# my_canvas.create_line(0, 100, 300, 100, fill="red")
# my_canvas.create_line(150, 0, 150, 200, fill="red")
my_canvas.bind('<B1-Motion>', paint)

root.mainloop()

