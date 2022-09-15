from tkinter import *

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
    draw_square(c, 'red', 100, (50, 50))
    draw_square(c, 'green', 100, (750, 50))
    draw_square(c, 'blue', 100, (50, 750))
    draw_square(c, 'yellow', 100, (750, 750))
    root.mainloop()
