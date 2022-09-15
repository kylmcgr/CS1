'''
lab3c_draw.py:
    Drawing commands needed to render drawings made by the lab 3 code.
'''

import sys
from turtle import *

def loadDrawing(filename):
    '''
    Load the drawing information and the bounding box from 'filename'.
    Return the bounds as an (xmin, xmax, ymin, ymax) tuple and
    the list of drawing commands.
    '''
    try:
        f = open(filename, 'r')
        bounds = f.readline()
        bounds = bounds.split()
        assert len(bounds) == 4
        bounds = map(float, bounds)
        cmds = []
        for line in f:
            next = line.split()
            assert (len(next) == 2 and next[0] in ['F', 'L', 'R']) or \
              (len(next) == 4 and next[0] == 'G')
            if next[0] in ['F', 'L', 'R']:
                next[1] = int(next[1])
            else:   # 'G'
                next[1] = float(next[1])
                next[2] = float(next[2])
                next[3] = float(next[3])
            cmds.append(next)
        return (bounds, cmds)
    except FileNotFoundError:
        print('ERROR: file not found: {}'.format(filename), file=sys.stderr)
        sys.exit(1)

def drawPicture(bounds, cmds, fast=False):
    '''
    Given the bounds and the drawing commands, draw the picture.
    '''

    (xmin, xmax, ymin, ymax) = bounds
    assert xmin <= xmax
    assert ymin <= ymax

    reset()

    hideturtle()
    speed(0)       # fastest
    if fast:
        tracer(0)  # no tracing

    xscale = float(xextent) / (float(xmax - xmin) * 1.3)
    yscale = float(yextent) / (float(ymax - ymin) * 1.3)
    scale  = min(xscale, yscale)
    xorigin = int(scale * (xmin + (xmax - xmin) / 2))
    yorigin = int(scale * (ymin + (ymax - ymin) / 2))

    penup()
    goto(-xorigin, -yorigin)
    pendown()

    counter = 1
    for cmd in cmds:
        if cmd[0] == 'L':
            left(cmd[1])
        elif cmd[0] == 'R':
            right(cmd[1])
        elif cmd[0] == 'F':
            forward(scale * cmd[1])
            counter += 1
        else:  # cmd[0] == 'G':
            penup()
            new_x = -xorigin + scale * cmd[1]
            new_y = -yorigin + scale * cmd[2]
            goto(new_x, new_y)
            setheading(cmd[3])
            pendown()

def usage():
    usageMsg = 'usage: python3 {} [-fast] filename [filename2 ...]'
    print(usageMsg.format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()

    fast = sys.argv[1] == '-fast'

    if fast:
        files = sys.argv[2:]
    else:
        files = sys.argv[1:]

    if not files:
        usage()

    xextent = 800
    yextent = 800
    setup(xextent, yextent)

    for file in files:
        bounds, cmds = loadDrawing(file)
        drawPicture(bounds, cmds, fast)
        update()
        input('Hit return to continue...')

