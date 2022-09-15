from functools import reduce
# Ex A.1.1
def union(a, b):
    '''Union takes two sets and returns a set of the union the sets.'''
    u = set()
    for i in a:
        u.add(i)
    for i in b:
        u.add(i)
    return u

# Ex A.1.2
def intersection(a, b):
    '''Intersection takes two sets and returns a set of the intersection the sets.'''
    u = set()
    for i in a:
        if i in b:
            u.add(i)
    return u

# Ex A.1.3
def difference(a, b):
    '''Difference takes two sets and returns a set of the difference the sets.'''
    u = set()
    for i in a:
        if i not in b:
            u.add(i)
    return u

# Ex A.2
def mySum(*nums):
    '''MySum takes an arbitrary number of positive integers and returns their
    sum'''
    s = 0
    for i in nums:
        if type(i) is not int:
            raise TypeError('inputs must be integers')
        if i <= 0:
            raise ValueError('inputs must be > 0')
        s += i
    return s

# Ex A.3
def myNewSum(*nums):
    '''MyNewSum takes a single list or an arbitrary number of positive integers
    and returns their sum'''
    s = 0
    if len(nums) == 1 and type(nums[0]) is list:
        nums = nums[0]
    for i in nums:
        if type(i) is not int:
            print(type(i))
            raise TypeError('inputs must be integers or a list of integers')
        if i <= 0:
            raise ValueError('inputs must be > 0')
        s += i
    return s

# Ex A.4
def myOpReduce(nums, **kw):
    '''MyOpReduce takes a list of numbers and an operator and returns the
    value of the operator performed on the list of numbers.'''
    if len(kw) == 0:
        raise ValueError('no keyword argument')
    if len(kw) > 1:
        raise ValueError('too many keyword arguments')
    if 'op' not in kw:
        raise ValueError('invalid keyword argument')
    if type(kw['op']) is not str:
        raise TypeError("value for keyword argument 'op' must be a string")
    if kw['op'] not in ['+', '*', 'max']:
        raise ValueError('invalid keyword argument2')
    if kw['op'] == '*':
        return reduce(lambda x, y: x * y, nums, 1)
    if nums == []:
        return 0
    if kw['op'] == '+':
        return sum(nums)
    if kw['op'] == 'max':
        return max(nums)

# Ex B.1
# Just return the sum and the function calling this will handle the errors
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    return dict[key1] + dict[key2]

# Ex B.2
# Just return the sum and the function calling this will handle the errors
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    return dict[key1] + dict[key2]

# Ex B.3
# Just return the sum and the function calling this will handle the errors
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    return dict[key1] + dict[key2]

# Ex B.4
# Just return the sum and the function calling this will handle the errors
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    return dict[key1] + dict[key2]

# Ex B.5
# Since the print statement is after the error being raised, it won't be printed
# so the message should be inside the error.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex B.6
# It's easier to read and better formatted to have the message inside the error.
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex B.7
# Should be a ValueError instead of a TypeError
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)

# Ex B.8
# Should have more specific errors
from math import exp

def exp_x_over_x(x):
    '''
    Return the value of e**x / x, for x > 0.0 and
    e = 2.71828... (base of natural logarithms).
    '''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0.0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)
