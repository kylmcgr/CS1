import random

# 4.B.1
def random_size(lower, upper):
     '''Generates a random even number between the bounds. Inputs are two even
     integers, and the output is a random even number between the inputs.'''
     assert(lower >= 0 and upper >= 0)
     assert(lower % 2 == 0 and upper % 2 == 0)
     assert(lower < upper)
     num = 2 * random.randint(lower / 2, upper / 2)
     assert(num % 2 == 0)
     return num

# 4.B.2
def random_position(max_x, max_y):
    '''Generates a random position. Inputs are two integers, and the output is
    a tuple of two random numbers between 0 and the respective inputs.'''
    assert(max_x >= 0 and max_y >= 0)
    return (random.randint(0, max_x), random.randint(0, max_y))

# 4.B.3
def random_color():
    '''Generates a random hex color. No inputs, and output is a string
    representing a hex color code.'''
    color = "#"
    c = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in range(6):
        color += random.choice(c)
    return color

# 4.B.4
def count_values(dict):
    '''Counts the number of unique values in a dictionary. Input is a
    dictionary, and output is the number of different values in it.'''
    vals = []
    for i in dict.values():
        if i not in vals:
            vals.append(i)
    return len(vals)

# 4.B.5
def remove_value(dict, val):
    '''Removes all instances of a value from a dictionary. Inputs are the
    dictionary and a value, and there is no output.'''
    keys = []
    for key in dict:
        if dict[key] == val:
            keys.append(key)
    for key in keys:
        del dict[key]

# 4.B.6
def split_dict(dict):
    '''Splits a dictionary by the values of the keys around n. Input is a
    dictionary, and outputs are a tuple of two dictionaries that is the input
    split by the keys around n'''
    dict1 = {}
    dict2 = {}
    for key in dict:
        if key[0].lower() <= 'n':
            dict1[key] = dict[key]
        else:
            dict2[key] = dict[key]
    return(dict1, dict2)

# 4.B.7
def count_duplicates(dict):
    '''Counts the number of values that appear multiple times in a dictionary.
    Input is a dictionary, and the output is number of values that appear
    multiple times.'''
    vals = list(dict.values())
    num = 0
    for i in vals:
        if vals.count(i) > 1:
            num += 1/vals.count(i)
    return int(num)
