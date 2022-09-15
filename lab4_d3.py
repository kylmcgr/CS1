from tkinter import *
import random

def random_size(lower, upper):
     '''Generates a random even number between the bounds. Inputs are two even
     integers, and the output is a random even number between the inputs.'''
     assert(lower >= 0 and upper >= 0)
     assert(lower % 2 == 0 and upper % 2 == 0)
     assert(lower < upper)
     num = 2 * random.randint(lower / 2, upper / 2)
     assert(num % 2 == 0)
     return num

def random_position(max_x, max_y):
    '''Generates a random position. Inputs are two integers, and the output is
    a tuple of two random numbers between 0 and the respective inputs.'''
    assert(max_x >= 0 and max_y >= 0)
    return (random.randint(0, max_x), random.randint(0, max_y))

def random_color():
    '''Generates a random hex color. No inputs, and output is a string
    representing a hex color code.'''
    color = "#"
    c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += random.choice(c)
    return color

def draw_square(canvas, color, width, position):
    '''Draws a square of some color and width at some position on the canvas.
    Inputs are the canvas to draw on, the color and width of the square, and
    a tuple of the center of the square, and the outputs is the handle of the
    create_rectangle function for the square.'''
    x, y = position
    return canvas.create_rectangle(x - width / 2, y - width / 2, x + width / 2,
    y + width / 2, fill=color, outline=color)

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    c = Canvas(root, width=800, height=800)
    c.pack()
    for i in range(50):
        draw_square(c, random_color(), random_size(20, 150), random_position(800, 800))
    root.bind('<q>', quit)
    root.mainloop()
