from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Python Tkinter Paint')
root.geometry("800x800")

def paint(event):

    # Brush params
    brush_width = '%0.0f' % float(my_slider.get())
    brush_color = "green"
    
    # Brush Type: BUTT, ROUND, PROJECTING
    brush_type = PROJECTING

    # Starting position
    x1 = event.x - 1
    y1 = event.y - 1

    # Ending position
    x2 = event.x + 1
    y2 = event.y + 1

    # Draw on the canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type, smooth=True)

# Change the size of the brush
def change_brush_size(thing):
    slider_label.config(text='%0.0f' % float(my_slider.get()))

def change_brush_color(thing):
    pass

def change_canvas_color(thing):
    pass

# Create our canvas
w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# my_canvas.create_line(0, 100, 300, 100, fill="red")
# my_canvas.create_line(150, 0, 150, 200, fill="red")
my_canvas.bind('<B1-Motion>', paint)

# Create brush option frames
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)
    
# Brush size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0, padx=50)

# Brush slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Brush type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type", height=400)
brush_type_frame.grid(row=0, column=1, padx=50)
brush_type = StringVar()
brush_type.set("round")

brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change colors
change_colors_frame = LabelFrame(brush_options_frame, text="Change Colors")
change_colors_frame.grid(row=0, column=2)

# Change Brush Color Button
brush_color_button = Button(change_colors_frame, text="Brush Color", command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# Change Canvas Background Color
canvas_color_button = Button(change_colors_frame, text="Canvas Color", command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

root.mainloop()
