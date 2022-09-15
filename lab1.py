# Problem 1:
# 9 - 3 = 6
# 8 * 2.5 = 20.0
# 9 / 2 = 4.5
# 9 / -2 = -4.5
# 9 % 2 = 1
# 9 % -2 = -1
# -9 % 2 = 1
# 9 / -2.0 = -4.5
# 4 + 3 * 5 = 19
# (4 + 3) * 5 = 35

# Problem 2:
# x = 100 --> x = 100
# x = x + 10 --> x = 110
# x += 20 --> x = 130
# x = x - 40 --> x = 90
# x -= 50 --> x = 40
# x *= 3 --> x = 120
# x /= 5 --> x = 24.0
# x %= 3 --> x = 0.0

# Problem 3:
# Evaluating x += x - x
# the first step is evaluating the value of x - x
# then the value of x - x is added to x
# when x has the initial value of 3:
# x - x is evaluted to be 3 - 3 = 0
# 0 is then added to the initial value of x
# x = x + 0
# x = 3 + 0 = 3
# after the statement has been evaluted:
# x will remain the same as its initial value
# an initial value of x = 3 will give x = 3

# Problem 4:
# 1j + 2.4j = 3.4j
# 4j * 4j = (-16+0j)
# (1+2j) / (3+4j) = (0.44+0.08j)
# (1+2j) * (1+2j) = (-3+4j)
# 1+2j * 1+2j = (1+4j)
# This leads me to believe that:
# complex numbers must have parentheses around them
# without parentheses they are treated as individual real and imaginary numbers
# so multiplying 1+2j * 1+2j will be the same as 1 + (2j * 1) + 2j
# or 1 + 2j + 2j = (1+4j)
# with parentheses, they are treated as compex numbers
# so multiplying (1+2j) * (1+2j) will foil them to get (-3+4j)

# Problem 5
# cmath.sin(-1.0+2.0j) = (-3.165778513216168+1.959601041421606j)
# cmath.log(-1.0+3.4j) = (1.2652585805200263+1.856847768512215j)
# cmath.exp(-cmath.pi * 1.0j) = (-1-1.2246467991473532e-16j)
# it is definitely better to write:
# import math
# import cmath
# because these two math module will definitely have name clashes
# from math import *
# from cmath import *
# doing this will cause functions (such as sqrt) to clashes
# so only the complex math functions that clash will be usable

# Prolem 6
# "foo" + 'bar' = 'foobar'
# "foo" 'bar' = 'foobar'
# a = 'foo'
# b = "bar"
# a + b = 'foobar'
# a = 'foo'
# b = "bar"
# a b = SyntaxError: invalid syntax

# Problem 7
# '''A
# B
# C'''
# 'A\nB\nC'

# Problem 8
# '-' * 80

# Problem 9
# first line
# second line
# third line
# "first line\nsecond line\nthird line"

# Problem 10
# The rabbit is 3.
# The rabbit is 3 years old.
# 12.5 is average.
# 12.5 * 3
# 12.5 * 3 is 37.5.
x = 3
y = 12.5
print("The rabbit is {}.".format(x))
print("The rabbit is {} years old.".format(x))
print("{} is the average.".format(y))
print("{} * {}".format(y,x))
print("{} * {} is {}.".format(y,x,x*y))

# Problem 11
num = float(input("Enter a number: "))
print(num)

# Problem 12
def quadratic(a, b, c, x):
    return a*x**2 + b*x + c

# Problem 13
def GC_content(dna):
    '''GC_content will calculate the ratio of G and C bases to the total
    number of bases in dna. The input should be a string of 'G' 'C' 'A' 'T'
    and the output represents the ratio of G and C to the total string'''
    G = dna.count('G')
    C = dna.count('C')
    GC_percent = (G+C)/len(dna)
    return GC_percent
