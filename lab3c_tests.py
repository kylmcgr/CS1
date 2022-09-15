# lab3c_tests.py

import nose
from lab3c import *

SMALL = 1.0e-4

# ---------------------------------------------------------------------- 
# Data we need for testing.
# ---------------------------------------------------------------------- 

#
# L-system strings.
#

# Koch snowflake.
k1 = 'F-F++F-F++F-F++F-F++F-F++F-F'
k2 = 'F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F'
k3 = 'F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F-F-F++F-F-F-F++F-F++F-F++F-F-F-F++F-F'

#
# Lists of drawing commands.
#

# Koch snowflake.
kc1 = ['F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1']
kc2 = ['F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'L 60', 'F 1', 'R 60', 'R 60', 'F 1', 'L 60', 'F 1']

#
# Bounds.
#

# Koch snowflake.
kb1 = (-6.661338147750939e-16, 3.0, -2.598076211353315, 0.8660254037844386)
kb2 = (-2.220446049250313e-16, 9.0, -7.794228634059945, 2.598076211353316)

#
# Lists of locations.
#

# Koch snowflake.
klocs1 = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (1.0, 0.0, 60.0), (1.5, 0.8660254037844386, 60.0), (1.5, 0.8660254037844386, 0.0), (1.5, 0.8660254037844386, 300.0), (2.0, 0.0, 300.0), (2.0, 0.0, 0.0), (3.0, 0.0, 0.0), (3.0, 0.0, 300.0), (3.0, 0.0, 240.0), (2.4999999999999996, -0.8660254037844384, 240.0), (2.4999999999999996, -0.8660254037844384, 300.0), (2.9999999999999996, -1.732050807568877, 300.0), (2.9999999999999996, -1.732050807568877, 240.0), (2.9999999999999996, -1.732050807568877, 180.0), (1.9999999999999996, -1.7320508075688767, 180.0), (1.9999999999999996, -1.7320508075688767, 240.0), (1.4999999999999991, -2.598076211353315, 240.0), (1.4999999999999991, -2.598076211353315, 180.0), (1.4999999999999991, -2.598076211353315, 120.0), (0.9999999999999993, -1.7320508075688763, 120.0), (0.9999999999999993, -1.7320508075688763, 180.0), (-6.661338147750939e-16, -1.732050807568876, 180.0), (-6.661338147750939e-16, -1.732050807568876, 120.0), (-6.661338147750939e-16, -1.732050807568876, 60.0), (0.49999999999999944, -0.8660254037844375, 60.0), (0.49999999999999944, -0.8660254037844375, 120.0), (-3.3306690738754696e-16, 1.3322676295501878e-15, 120.0)]

# ---------------------------------------------------------------------- 
# Helper functions.
# ---------------------------------------------------------------------- 

def floatEquals(f1, f2):
    '''
    Compare two floats for equality.
    '''
    return (abs(f1 - f2) < SMALL)

def compareDrawingCommandLists(l1, l2):
    '''
    Return True if the lists 'l1' and 'l2' contain the same drawing
    commands.
    '''
    if len(l1) != len(l2):
        return False
    for i, _ in enumerate(l1):
        line1 = l1[i].split()
        line2 = l2[i].split()
        if line1[0] != line2[0]:
            return False
        for (s1, s2) in zip(line1[1:], line2[1:]):
            v1 = float(s1)
            v2 = float(s2)
            if abs(v1 - v2) >= SMALL:
                return False
    return True

def compareTuples(t1, t2, l):
    '''
    Return True if the tuples 't1' and 't2' contain the same values
    (within a certain tolerance). 'l' is the expected tuple length.
    '''
    if len(t1) != len(t2):
        return False
    if len(t1) != l:
        return False
    for (x, y) in zip(t1, t2):
        if abs(x - y) >= SMALL:
            return False
    return True

def compareBounds(b1, b2):
    '''
    Return True if the bounds 'b1' and 'b2' contain the same values
    (within a certain tolerance).
    '''
    return compareTuples(b1, b2, 4)

def compareLocations(l1, l2):
    '''
    Return True, if locations 'l1' and 'l2' contain the same values
    (within a certain tolerance).
    '''
    return compareTuples(l1, l2, 3)

def allLocations(cmds):
    '''
    Return a list of all the locations/angles encountered while 
    executing a list of commands.
    '''
    loc = (0.0, 0.0, 0.0)
    locs = [loc]
    for cmd in cmds:
        next_loc = nextLocation(loc[0], loc[1], loc[2], cmd)
        locs.append(next_loc)
        loc = next_loc
    return locs

def compareListOfLocations(cmds1, cmds2):
    if len(cmds1) != len(cmds2):
        return False
    for l1, l2 in zip(cmds1, cmds2):
        if not compareLocations(l1, l2):
            return False
    return True

# ---------------------------------------------------------------------- 
# The tests themselves.
# ---------------------------------------------------------------------- 

def test_update():
    assert update(koch, koch['start']) == k1
    assert update(koch, k1) == k2
    assert update(koch, k2) == k3

def test_iterate():
    assert iterate(koch, 1) == k1
    assert iterate(koch, 2) == k2
    assert iterate(koch, 3) == k3

def test_lsystemToDrawingCommands():
    assert compareDrawingCommandLists(
             lsystemToDrawingCommands(koch_draw, iterate(koch, 1)), kc1)
    assert compareDrawingCommandLists(
             lsystemToDrawingCommands(koch_draw, iterate(koch, 2)), kc2)

def test_bounds():
    assert compareBounds(bounds(kc1), kb1)
    assert compareBounds(bounds(kc2), kb2)

def test_nextLocation():
    assert compareLocations(nextLocation(0.0, 0.0, 0.0, 'F 1'),  
      (1.0, 0.0, 0.0))
    assert compareLocations(nextLocation(0.0, 0.0, 0.0, 'L 10'), 
      (0.0, 0.0, 10.0))
    assert compareLocations(nextLocation(0.0, 0.0, 0.0, 'R 10'), 
      (0.0, 0.0, 350.0))
    assert compareListOfLocations(klocs1, allLocations(kc1))

def test_saveDrawing():
    saveDrawing('koch_2', kb2, kc2)
    f = open('koch_2', 'r')
    lines = f.readlines()
    f.close()
    b2 = tuple(map(float, lines[0].split()))
    assert compareBounds(b2, kb2)
    assert compareDrawingCommandLists(lines[1:], kc2)

if __name__ == '__main__':
    nose.runmodule()


