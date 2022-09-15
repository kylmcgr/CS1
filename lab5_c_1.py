from tkinter import *
import random

# Graphics commands.

def random_color():
    '''Generates a random hex color.'''
    color = "#"
    c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += random.choice(c)
    return color

def draw_circle(x, y):
    '''Draws a circle on the canvas.'''
    r = random.randint(5, 25)
    return canvas.create_oval(x - r, y - r, x + r,
    y + r, fill=color, outline=color)

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global circles
    global color
    if event.keysym == 'q':
        quit()
    if event.keysym == 'c':
        color = random_color()
    if event.keysym == 'x':
        for circle in circles:
            canvas.delete(circle)
        circles = []

def button_handler(event):
    '''Handle left mouse button click events.'''
    # global circles
    circles.append(draw_circle(event.x, event.y))

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    circles = []
    color = random_color()

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
