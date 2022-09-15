import math

# Ex A.1
class Point:
    '''This class represents a point in three-dimensional Euclidean space.'''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, point):
        '''Computes the distance between this point and the point given.'''
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 +
        (self.z - point.z) ** 2)

# Ex A.2
class Triangle:
    '''This class represents a triagle as three points.'''
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
        '''Computes the area of the triangle.'''
        a = self.p1.distanceTo(self.p2)
        b = self.p2.distanceTo(self.p3)
        c = self.p3.distanceTo(self.p1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Ex A.3
class Averager:
    '''This class represents a list and performs various actions on the list.'''
    def __init__(self):
        self.nums = []
        self.total = 0
        self.n = 0

    def getNums(self):
        '''Returns a copy of the list.'''
        return self.nums.copy()

    def append(self, num):
        '''Appends a number to the list.'''
        self.nums.append(num)
        self.total += num
        self.n += 1

    def extend(self, nums):
        '''Appends a list of numbers to the list.'''
        self.nums += nums
        self.total += sum(nums)
        self.n += len(nums)

    def average(self):
        '''Returns a float of the average of the list.'''
        if self.n == 0:
            return 0.0
        return float(self.total) / self.n

    def limits(self):
        '''Returns a tuple of the max and min of the list.'''
        if self.n == 0:
            return (0, 0)
        return (min(self.nums), max(self.nums))


# Ex B.1
# The else is unecessary code since if the code goes inside the if statement,
# then the function will return and won't reach past the if statement. Can also
# be simplified as a boolean expression.
def is_positive(x):
    '''Test if x is positive.'''
    return x > 0

# Ex B.2
# The found variable is unecessary inefficient code since returning the index
# once the item is found will exit out of the function. The location variable
# is also unecessary since we will be returning the value as soon as we find it
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# Ex B.3
# If x is in one of the categories, it is unecessary and inefficient to check
# the other categories and the value should just be returned.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    if x == 0:
        return 'zero'
    if x > 0 and x < 10:
        return 'small'
    return 'large'

# Ex B.4
# The if statements are unecessary and inefficient code as the last part of the
# function will work for lists of length 0, 1, and 2 as well.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    total = 0
    for item in lst:
        total += item
    return total
