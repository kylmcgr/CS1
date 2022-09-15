import random

# Ex B.1:
def complement(dna):
    """complement will create the complement to a strand of DNA.
    The input should be a string of 'A', 'C', 'G', and 'T' and
    the output represents the complement to that string."""
    comp = ''
    for letter in dna:
        if letter == 'A':
            comp += 'T'
        elif letter == 'T':
            comp += 'A'
        elif letter == 'C':
            comp += 'G'
        elif letter == 'G':
            comp += 'C'
    return comp

# Ex B.2:
def list_complement(dna):
    """list_complement will create the complement to a strand of DNA.
    The input should be a list of 'A', 'C', 'G', and 'T' and there will
    be no output but the list will be changed into the compliment of
    that dna."""
    for i in range(len(dna)):
        if dna[i] == 'A':
            dna[i] = 'T'
        elif dna[i] == 'T':
            dna[i] = 'A'
        elif dna[i] == 'C':
            dna[i] = 'G'
        elif dna[i] == 'G':
            dna[i] = 'C'

# Ex B.3:
def product(nums):
    """product will compute the product of a set of numbers.
    The input should be a list of numbers, and the output
    will be the product of those numbers."""
    prod = 1
    for num in nums:
        prod *= num
    return prod

# Ex B.4:
def factorial(num):
    """factorial will compute the factorial of a number.
    The input should be a number, and the output will
    be the factorial of that number."""
    return product(range(1, num + 1))

# Ex B.5
def dice(m, n):
    """dice will roll n dice each with m sides. The
    input should be two numbers for the number of sides
    on each dice and number of dice, and the output will
    be the sum of all the dice rolls"""
    total = 0
    for i in range(n):
        total += random.choice(range(1, m + 1))
    return total

# Ex B.6
def remove_all(list, num):
    """remove_all will remove all instances of a number
    from a list of numbers. Inputs should be a list of
    numbers and a number, and there will be no output
    but the list will have all of the number removed."""
    while(list.count(num) > 0):
        list.remove(num)

# Ex B.7
def remove_all2(list, num):
    """remove_all2 will remove all instances of a number
    from a list of numbers. Inputs should be a list of
    numbers and a number, and there will be no output
    but the list will have all of the number removed."""
    for i in range(list.count(num)):
        list.remove(num)

def remove_all3(list, num):
    """remove_all3 will remove all instances of a number
    from a list of numbers. Inputs should be a list of
    numbers and a number, and there will be no output
    but the list will have all of the number removed."""
    while(num in list):
        list.remove(num)

# Ex B.8
def any_in(list1, list2):
    """any_in will determine in any elements of one list
    are in the other list. The inputs should be two lists,
    and the output is true if any element of the first list
    is in the second list and false otherwise."""
    for element in list1:
        if element in list2:
            return True
    return False

# Ex C.1.a
# The incorrect part of the progam is the part in the if statement
# that checks if a is equal to 0. It is incorrect because it only
# has 1 equals sign which is for assigning, but it needs to have the
# double equals sign to evaluate the expression
# if a == 0:

# Ex C.1.b
# The problem with this code is in the parameter of the function.
# The variable s is put in single quotes in the parameter of the
# function so the function will not be able to take in a string
# as input. Getting rid of the single quotes will allow an input
# to be given and stored in s.
# def add_suffix(s):

# Ex C.1.c
# The problem with this code is in the return of the function.
# The variable s is put in single quotes in the return of the
# function so the function will use the input string but rather
# use the string 's'. Getting rid of the single quotes will allow
# the input string to be used and returned.
# return s + '-Caltech'

# Ex C.1.d
# The problem with this code is that the + operator can only be
# used with a list if its adding another list. Since it is adding
# a string to a list, we get an error. We can fix this by using
# the append function instead of the + operator or by putting
# brackets around the string so that we are adding two lists.
# lst.append('bam') OR lst += ['bam']

# Ex C.1.e
# The problem with this is that the function returns the append
# function rather than the list. The append function has no return
# value so the function will return None. Since the reverse function
# also works like this, we can fix this by moving running the append
# and the reverse then returning the list.
# lst.reverse().append(0)
# return lst

# Ex C.1.f
# This code appends a list to a list; this doesn't create a list with
# the elements of both lists as we want but rather puts the entire
# list as a single element in the other list. To fix this we can
# instead use the + operator to added the lists. Additionally, the
# parameters are named with reserved words (list, str) so we have
# to change them to valid variable names such as lst and string.
# lst += letters

# Ex C.2
# This code gives 30 rather than 50 because c is evaluated before
# a is changed to 30. C will be evaluated to be 10 + 20 and a is
# changed after the value of c is determined. You would have to
# change the value of a before computing c to get 50.
# a = 30
# c = b + a


# Ex C.3
# Having a return statement in a function with allow it to give
# back a value when it is called. Ending a function with a print
# statement will allow you to see the value, but in order to get
# it back when calling the function you have to return the value.
# return result

# Ex C.4
# Using input will allow you to interactively give values while
# the program runs but won't allow you to pass values into the
# function. To do this, the variable have to be parameters in the
# function.
# def sum_of_squares_1(x, y):

# Ex C.5
# While strings are similar lists of characters and s[0] can get
# the first chracter of s, this function won't work because you
# can't assign values to characters in the string. You would
# have to change the first character then re-add it to the string.
# s = s[0].upper()+s[1:]

# Ex C.6
# When you use this kind of for loop that goes through each
# element of a list, the items are equal to the values of the
# elements in the list but don't actually point to those elements.
# This means that you will be changing the temporary variable
# rather than the element in the list. To change the element in the
# list you would have to going through the indices of the list instead.
# for i in range(len(lst)):
#   lst[i] *= 2
