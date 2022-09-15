from tkinter import *
import random
import math

# Graphics commands.

def random_color():
    '''Generates a random hex color.'''
    color = "#"
    c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += random.choice(c)
    return color

def draw_star(x, y):
    '''Draws a star on the canvas.'''
    lines = []
    r = random.randint(25, 50)
    for i in range(N):
        angle1 = (math.pi * 2.0 / N) * (i) + math.pi / 2.0
        p1 = [r * math.cos(angle1), r * math.sin(angle1)]
        angle2 = (math.pi * 2.0 / N) * ((i + (N - 1) / 2) % N) + math.pi / 2.0
        p2 = [r * math.cos(angle2), r * math.sin(angle2)]
        lines.append(canvas.create_line(x + p1[0], y - p1[1], x + p2[0], y - p2[1],
        fill=color))
    return lines

# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    global stars
    global color
    global N
    if event.keysym == 'q':
        quit()
    if event.keysym == 'c':
        color = random_color()
    if event.keysym == 'x':
        for star in stars:
            for line in star:
                canvas.delete(line)
        stars = []
    if event.keysym == 'plus':
        N += 2
    if event.keysym == 'minus' and N >= 7:
        N -= 2

def button_handler(event):
    '''Handle left mouse button click events.'''
    # global circles
    stars.append(draw_star(event.x, event.y))

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    stars = []
    color = random_color()
    N = random.randint(2, 10) * 2 + 1

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
