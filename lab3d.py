'''
lab3d.py
Copy of lab3c.py with brackets.
'''

# References:
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/

import math

# ----------------------------------------------------------------------
# Example L-systems.
# ----------------------------------------------------------------------

# Koch snowflake.
koch = { 'start' : 'F++F++F',
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1',
              '+' : 'R 60',
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A',
             'A'     : '-BF+AFA+FB-' ,
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1',
                 '-' : 'L 90',
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G',
               'F'     : 'F-G+F+G-F',
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1',
                    'G' : 'F 1',
                    '+' : 'L 120',
                    '-' : 'R 120' }

# plant structure
plant = { 'start' : 'X',
          'X'     : 'F-[[X]+X]+F[+FX]-X',
          'F'     : 'FF' }

plant_draw = { 'F' : 'F 1',
               '-' : 'L 25',
               '+' : 'R 25' }

# ----------------------------------------------------------------------
# L-systems functions.
# ----------------------------------------------------------------------

def update(lsys, s):
    '''updates the string with the given dictionary. The inputs are the
    dictionary of rules and the current string, and the output is the new
    string with the rules appled'''
    newS = ""
    for letter in s:
        if letter in lsys:
            newS += lsys[letter]
        else:
            newS += letter
    return newS

def iterate(lsys, n):
    '''iterates the starting string in the dictionary n times through the
    rules. The inputs are the dictionary of rules and the number of times to
    iterate, and the output is the string after that many iterations.'''
    s = lsys['start']
    for i in range(n):
        s = update(lsys, s)
    return s

def nextLocation(x, y, angle, cmd):
    '''gives the next location of the turtle after the command has been
    executed. The inputs are the current x, y, and angle of the turtle as well
    as the command to run, and the output is the next x, y, and angle.'''
    cmds = cmd.split()
    newX = x
    newY = y
    newAngle = angle
    if cmds[0] == 'F':
        newX += math.cos(newAngle * (math.pi / 180)) * int(cmds[1])
        newY += math.sin(newAngle * (math.pi / 180)) * int(cmds[1])
    elif cmds[0] == 'R':
        newAngle -= int(cmds[1])
    elif cmds[0] == 'L':
        newAngle += int(cmds[1])
    elif cmds[0] == 'G':
        newX = float(cmds[1])
        newY = float(cmds[2])
        newAngle = int(cmds[3])
    newAngle = newAngle % 360
    return (newX, newY, newAngle)

def lsystemToDrawingCommands(draw, s):
    '''changes the L-system string into the corresponding set of drawing
    instructions. The inputs are the drawing dictionary and the string to draw
    from, and the output is a list of the corresponding drawing commands.'''
    cmds = []
    locations = []
    for letter in s:
        if letter in draw:
            cmds.append(draw[letter])
        elif letter == '[':
            x = 0.0
            y = 0.0
            angle = 0
            for cmd in cmds:
                x, y, angle = nextLocation(x, y, angle, cmd)
            location = (x, y, angle)
            locations.append(location)
        elif letter == ']':
            cmds.append('G '+' '.join(str(i) for i in locations.pop()))
    return cmds

def bounds(cmds):
    '''computes the bounds of the drawing made by the commands given. The input
    is a list of commands, and the output is a tuple containing the min and max
    values of x and y.'''
    x = 0.0
    y = 0.0
    angle = 0
    xmin = 0.0
    xmax = 0.0
    ymin = 0.0
    ymax = 0.0
    for cmd in cmds:
        x, y, angle = nextLocation(x, y, angle, cmd)
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return (xmin, xmax, ymin, ymax)

def saveDrawing(filename, bounds, cmds):
    '''writes the bounds and commands for a drawing to a file. The inputs are
    a string of the name of the file, a tuple of the bounds, and a list of the
    commands, and a file is created with all the information.'''
    file = open(filename, 'w')
    file.write(' '.join(str(i) for i in bounds)+"\n")
    for cmd in cmds:
        file.write(cmd+"\n")
    file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print('Making drawings for {}...'.format(name))
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    # makeDrawings('koch', koch, koch_draw, 0, 6)
    # makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    # makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)
    makeDrawings('plant', plant, plant_draw, 1, 7)

main()
