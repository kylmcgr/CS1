# Ex A.1
def list_reverse(lst):
    '''reverses a list. Input is a list and output is the list in reverse'''
    lst2 = lst
    lst2.reverse()
    return lst2

# Ex A.2
def list_reverse2(lst):
    '''also reverses a list but without the reverse method. Input is a list
    and output is the list in reverse'''
    lst2 = []
    for i in range(len(lst) - 1, -1, -1):
        lst2.append(lst[i])
    return lst2

# Ex A.3
def file_info(filename):
    '''determines the number of lines, the number of words, and the number of
    characters in a file. Input is a file name and output is a tuple with the
    three values.'''
    numLines = 0
    numWords = 0
    numCharacters = 0
    file = open(filename, 'r')
    for line in file:
        numLines += 1
        numWords += len(line.split())
        numCharacters += len(line)
    file.close()
    return (numLines, numWords, numCharacters)

# Ex A.4
def file_info2(filename):
    '''determines the number of lines, the number of words, and the number of
    characters in a file. Input is a file name and output is a dictionary with
    the three values.'''
    info = {}
    info['lines'], info['words'], info['characters'] = file_info(filename)
    return info

# Ex A.5
def longest_line(filename):
    '''finds the longest line in a file. Input is a file name and output is a
    tuple with length of the line and the line itself.'''
    file = open(filename, 'r')
    length = 0
    longLine = ""
    for line in file:
        if len(line)>length:
            longLine = line
            length = len(longLine)
    file.close()
    return (length, longLine)

# Ex A.6
def sort_words(string):
    '''sorts the words in a string. Input is a string and output is a sorted
    list of the words in the string.'''
    words = string.split()
    words.sort()
    return words

# Ex A.7
# 128, 64, 32, 16, 8, 4, 2, 1 value of each bit in binary to base 10
#  1   1   0   1   1  0  1  0 our binary number
# 128 + 64 + 16 + 8 + 2 = 218
#  1   1   1   1   1  1  1  1 largest binary number
# one less than than the next power of 2 so 255

# Ex A.8
def binaryToDecimal(binary):
    '''converts a binary number to a base 10 number. Input is a list with the
    digits of the binary number and the output is the number in base 10'''
    dec = 0
    for i in range(len(binary)):
        if binary[len(binary) - i - 1] == 1:
            dec += binary[len(binary) - i - 1] * (2 ** i)
    return dec

# Ex A.9
def decimalToBinary(dec):
    '''converts a base 10 number to a binary number. Input is an integer and
    the output is list of the digits of the binary number'''
    if dec == 0:
        return [0]
    binary = []
    start = 0
    while dec >= 2 ** start:
        start += 1
    start -= 1
    for i in range(start, -1, -1):
        if dec >= 2 ** i:
            binary.append(1)
            dec -= 2 ** i
        else:
            binary.append(0)
    return binary

# Ex B.2.1
# operator space, comma space, bad name
def sumCubes(a, b, c):
    return a * a * a + b * b * b + c * c * c

# Ex B.2.2
# comment space, line length, bad names, comment grammatical
def sumofcubes(a, b, c, d):
    # returns the sum of the cubes of a, b, c, and d
    return a * a * a + b * b * b + c * c * c + d * d * d

# Ex B.2.3
# blank lines, indent inconsistent
# 2 different kinds of style mistakes:
def sum_of_squares(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
   return x * x * x + y * y * y + z * z * z
