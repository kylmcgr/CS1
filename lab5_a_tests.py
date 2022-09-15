import nose
import math
from lab5_ab import *

# B.1
def close(x, y):
    return abs(x - y) < 1.0e-10

def test_Point():
    p1 = Point(0.0, 0.0, 0.0)
    p2 = Point(1.0, 0.0, 0.5)
    p3 = Point(0.0, 1.0, 0.5)
    assert close(p1.distanceTo(p2), 1.118033988749895)
    assert close(p1.distanceTo(p3), 1.118033988749895)
    assert close(p2.distanceTo(p2), 0.0)
    assert close(p2.distanceTo(p3), math.sqrt(2.0))
    assert close(p3.distanceTo(p1), 1.118033988749895)

# B.2
def test_Triangle():
    p1 = Point(0.0, 0.0, 0.0)
    p2 = Point(1.0, 0.0, 0.5)
    p3 = Point(0.0, 1.0, 0.5)
    t  = Triangle(p1, p2, p3)
    assert close(t.area(), 0.6123724356957944)

# B.3
def test_Averager():
    a = Averager()
    assert a.average() == 0
    assert a.getNums() == []
    assert a.limits() == (0, 0)
    a.append(1)
    a.append(2)
    a.append(3)
    a.extend(list(range(4, 11)))
    nums = a.getNums()
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Make sure 'nums' is a copy.
    nums[0] = 42
    nums = a.getNums()
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert close(a.average(), 5.5)
    assert a.limits() == (1, 10)

if __name__ == '__main__':
    nose.runmodule()


