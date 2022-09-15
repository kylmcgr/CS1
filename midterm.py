# Name: Kyle McGraw
# CMS cluster login name: kmcgraw

import random, sys, time

# ----------------------------------------------------------------------
# Part 1: Pitfalls
# ----------------------------------------------------------------------

#
# Problem 1.1
#

# Mistakes in the code:
# 1. The name of the variable that is supposed to be passed into the function is
# put in quotes when it shouldn't be: def fiblist('n'):
# 2. The condition in the if statement using a single assignment equals rather
# than a double equals to compare: if n = 0:
# 3. There needs to be a colon after the condition of the while statement:
# while True
# 4. The docstring and the code of the function are indented by different
# amounts, but they need consistent indentation.
# 5. The docstring is split onto multiple lines and is surrounded by single
# quotes, but single quotes can't be split onto multiple lines.


#
# Problem 1.2
#

# Mistakes in the code:
# 1. Dictionaries can't use lists as keys, so both of the lists used in the
# definition of substitutions are incorrect. Since the if statement later uses
# in rather than equals, these can just be a string rather than a list.
# 2. In the for loop over the line, the variable i is being used as an index,
# but is actually a tuple created from looping over the enumerate object.
# Either the enumerate should be changes to range(len(line)) or all future
# instances of i should be i[0]
# 3. Looping over the dictionary will only give all of the keys, but the code
# tries to get both the key and value. To unpack it into the key, value pair
# you would have to loop over substitutions.items()
# 4. The should be only 1 equals rather than 2 for done == True since you want
# to assign done to the value of True rather than check if done hold the value
# of True.
# 5. Both line[i] = sub and line [i] = char also will not work as strings are
# immutable and the individual characters of the string cannot be changed. You
# would have to create a new string with the changed character.


#
# Problem 1.3
#

# Mistakes in the code:
# 1. [OPERATOR_SPACE]: need spaces between the operators
# 2. [COMMA_SPACE]: need spaces after commas
# 3. [COMMENT_SPACE]: need a space after the #
# 4. [BAD_NAMES]: I have no idea what the function or variables do
# 5. [STMTS_ON_LINE]: put return on the same line as the if statement
# 6. [COMMENT_GRAMMATICAL]: I have no idea what the docstring is trying to say


# ----------------------------------------------------------------------
# Part 2: Simple functions.
# ----------------------------------------------------------------------

import random, sys

#
# Problem 2.1
#

def draw_checkerboard(nrows, ncols):
    '''
    Return a string that, when printed, will draw an (nrows x ncols)
    checkerboard on the terminal, where 'nrows' and 'ncols' are positive
    integers.

    The light squares are blank, the dark squares have a '#' character.
    The board is made up of lines and corners.
    Corners are represented by '+' characters.
    Horizontal lines are represented by '-' characters.
    Vertical lines are represented by '|' characters.
    The lower-left square of the bottommost row is black.

    Arguments:
      nrows: the number of rows
      ncols: the number of columns

    Return value: a string representing the checkerboard, suitable for printing
      to the terminal.  The string, when printed, will have a blank line before
      and after the checkerboard.

    '''

    assert nrows >= 1
    assert ncols >= 1
    board = "\n+" + ("-+" * ncols) + "\n"
    for i in range(nrows):
        board += "|"
        for j in range(ncols):
            board += " |" * ((nrows - i - j - 1) % 2)
            board += "#|" * ((nrows - i - j) % 2)
        board += "\n+" + ("-+" * ncols) + "\n"
    return board

def test_draw_checkerboard():
    print(draw_checkerboard(1, 1))
    print(draw_checkerboard(1, 2))
    print(draw_checkerboard(2, 1))
    print(draw_checkerboard(2, 2))

    print(draw_checkerboard(4, 4))
    print(draw_checkerboard(4, 5))
    print(draw_checkerboard(5, 4))
    print(draw_checkerboard(5, 5))

    print(draw_checkerboard(8, 8))


#
# Problem 2.2
#

def roll_count(lst):
    '''
    Return a dictionary containing the count of all numbers
    in the list.

    Argument: a list of length 5, of ints in the range [1-6]
    '''
    count = {}
    for i in lst:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count

def yahtzee_classify(lst):
    '''
    For a list of 5 numbers in the range 1-6, figure out which Yahtzee category
    they belong to.  The categories are:

      Yahtzee:         5 of one number
      Four of a kind:  4 of one number
      Full house:      3 of one number and 2 of another
      Large straight:  5 consecutive numbers
      Small straight:  4 consecutive numbers
      Three of a kind: 3 of one number
      Chance:          anything else

    The categories are mutually exclusive.  For instance, a Yahtzee is not
    also considered four of a kind or three of a kind, and a full house is
    not a three of a kind.  Always choose the highest possible rank for the
    hand.  Ranks are ordered (from high to low):

      Yahtzee > Four of a kind > Full house
        > Large straight > Small straight
        > Three of a kind > Chance

    Return the category as a string; one of:
      'YAHTZEE', 'FOUR OF A KIND', 'FULL HOUSE',
      'LARGE STRAIGHT', 'SMALL STRAIGHT',
      'THREE OF A KIND', 'CHANCE'
    '''
    roll = roll_count(lst)
    keys = list(roll.keys())
    keys.sort()
    if 5 in roll.values():
        return "YAHTZEE"
    elif 4 in roll.values():
        return "FOUR OF A KIND"
    elif 3 in roll.values() and 2 in roll.values():
        return "FULL HOUSE"
    elif keys == [1, 2, 3, 4, 5] or keys == [2, 3, 4, 5, 6]:
        return "LARGE STRAIGHT"
    elif small_straight(keys):
        return "SMALL STRAIGHT"
    elif 3 in roll.values():
        return "THREE OF A KIND"
    return "CHANCE"

def small_straight(keys):
    beg = keys[:4]
    end = keys[1:]
    if beg == [1, 2, 3, 4] or end == [1, 2, 3, 4]:
        return True
    if beg == [2, 3, 4, 5] or end == [2, 3, 4, 5]:
        return True
    if beg == [3, 4, 5, 6] or end == [3, 4, 5, 6]:
        return True
    return False

# Supplied to students.
def yahtzee_roll():
    '''
    Make a random roll of five dice and return a list of the results.
    '''

    lst = []
    for i in range(5):
        roll = random.randint(1, 6)
        lst.append(roll)
    lst.sort()
    return lst


#
# Problem 2.3
#


import random

def nim_done(lst):
    '''
    Return True if the list 'lst' contains all zeros.
    '''
    for i in lst:
        if i != 0:
            return False
    return True

def nim_sum(lst):
    '''
    Compute and return the Nim sum of a list of non-negative integers.
    The Nim sum is the exclusive or of all the items in the list.
    '''
    dimsum = 0
    for i in lst:
        dimsum ^= i
    return dimsum

def nim_random_move(lst):
    '''
    Make a random move in a Nim game.

    Argument: lst: the state of the game.

    Return value: a 2-tuple: (index of the random move, # to remove)
    '''
    indicies = []
    for i in range(len(lst)):
        if lst[i] > 0:
            indicies.append(i)
    move = random.choice(indicies)
    remove = random.randint(1, lst[move])
    return (move, remove)

def nim_best_move(lst):
    '''
    Compute the optimal nim move in a list of non-negative integers.
    Return the index of the list and how many to remove from that location.

    Argument: lst: the state of the game.

    Return value: a 2-tuple: (index of the best move, # to remove)
    '''
    dimsum = nim_sum(lst)
    move = nim_random_move(lst)
    for i in range(len(lst)):
        xor = dimsum ^ lst[i]
        if xor < lst[i]:
            return (i, lst[i] - xor)
    return move

#
# Supplied to students:
#

def nim_show(lst):
    '''
    Display a nim board.
    '''

    print('Nim: ', end='')
    for item in lst:
        print(item, end=' ')
    print('\n')  # two newlines

def nim_get_move(lst):
    '''
    Get a move from the player in a Nim game.  Do error checking.
    Repeat until a valid move is entered.
    '''

    try_again = 'Invalid move -- try again.\n'

    while True:
        move = input('Enter your move (index, n): ')
        move = move.split()

        # Error checking.
        if len(move) != 2:
            print('Error: input must be two numbers.')
            print(try_again)
            continue

        (i, n) = move

        try:
            i = int(i)
            n = int(n)
        except ValueError:
            print('Error: index and n must both be ints')
            print(try_again)
            continue

        if i < 0 or i > len(lst):
            print('Error: index out of range')
            print(try_again)
            continue

        if n <= 0:
            print('Error: number to be removed is too small')
            print(try_again)
            continue

        if lst[i] < n:
            print('Error: number to be removed is too large')
            print(try_again)
            continue

        return (i, n)


def nim_play(lst):
    '''
    Play a game of nim against the computer, given a starting list.
    '''

    while True:
        nim_show(lst)

        # Computer moves.
        (i, n) = nim_best_move(lst)
        print(f'Computer moves: {i} {n}\n')

        lst[i] -= n
        if nim_done(lst):
            print('Computer wins!')
            break

        nim_show(lst)

        # Human player moves.
        (i, n) = nim_get_move(lst)

        lst[i] -= n
        if nim_done(lst):
            print('You win!')
            break

# ----------------------------------------------------------------------
# Miniproject: The 3's game.
# ----------------------------------------------------------------------


#
# Problem 3.1
#

def make_board():
    '''
    Create a game board in its initial state.

    The board is a dictionary mapping (row, column) coordinates (zero-indexed)
    to integers which are all initially either 1, 2, or 3.  There are 4 rows and
    4 columns.  Empty locations are not stored in the dictionary.  Exactly 9
    randomly-chosen locations are initially filled. At least one each of 1, 2, 3
    must be present; the other six locations are filled at random with a 1, 2 or
    3.

    Arguments: none
    Return value: the board
    '''
    board = {}
    pos = []
    nums = [1, 2, 3]
    for row in range(4):
        for col in range(4):
            pos.append((row, col))
    random.shuffle(pos)
    for i in range(6):
        nums.append(random.randint(1, 3))
    for i in range(len(nums)):
        board[pos[i]] = nums[i]
    return board


#
# Problem 3.2
#

def get_row(board, row_n):
    '''
    Return a row of the board as a list of integers.
    Arguments:
      board -- the game board
      row_n -- the row number

    Return value: the row
    '''
    assert 0 <= row_n < 4
    row = []
    for i in range(4):
        row.append(board.get((row_n, i)))
        if row[i] == None:
            row[i] = 0
    return row

def get_column(board, col_n):
    '''
    Return a column of the board as a list of integers.
    Arguments:
      board -- the game board
      col_n -- the column number

    Return value: the column
    '''
    assert 0 <= col_n < 4
    col = []
    for i in range(4):
        col.append(board.get((i, col_n)))
        if col[i] == None:
            col[i] = 0
    return col

def put_row(board, row, row_n):
    '''
    Given a row as a list of integers, put the row values into the board.

    Arguments:
      board -- the game board
      row   -- the row (a list of integers)
      row_n -- the row number

    Return value: none; the board is updated in-place.
    '''
    assert 0 <= row_n < 4
    assert len(row) == 4
    for i in range(len(row)):
        if row[i] != 0:
            board[(row_n, i)] = row[i]
        elif (row_n, i) in board:
            del board[(row_n, i)]

def put_column(board, col, col_n):
    '''
    Given a column as a list of integers, put the column values into the board.

    Arguments:
      board -- the game board
      col   -- the column (a list of integers)
      col_n -- the column number

    Return value: none; the board is updated in-place.
    '''
    assert 0 <= col_n < 4
    assert len(col) == 4
    for i in range(len(col)):
        if col[i] != 0:
            board[(i, col_n)] = col[i]
        elif (i, col_n) in board:
            del board[(i, col_n)]

#
# Problem 3.3
#

def can_merge(n1, n2):
    '''
    Return True if two numbers can be merged according to the
    rules of the Threes game.
    '''
    if n1 + n2 == 3:
        return True
    if n1 >= 3 and n1 == n2:
        return True
    return False


def make_move_on_list(numbers):
    '''
    Make a move given a list of 4 numbers using the rules of the
    Threes game.

    Argument: numbers -- a list of 4 numbers
    Return value: the list after moving the numbers to the left.

    Note: the original list is not altered.
    '''

    assert len(numbers) == 4
    new = numbers
    for i in range(3):
        if can_merge(new[i], new[i + 1]):
            new[i] = new[i] + new[i + 1]
            new[i + 1] = 0
        elif new[i] == 0:
            new[i] = new[i + 1]
            new[i + 1] = 0
    return new

#
# Problem 3.4
#

def make_move(board, cmd):
    '''
    Make a move on a board given a movement command.
    Movement commands include:

      'w' -- move numbers upward
      's' -- move numbers downward
      'a' -- move numbers to the left
      'd' -- move numbers to the right

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''

    assert cmd in ['w', 'a', 's', 'd']
    if cmd == 'w':
        cols = []
        for i in range(4):
            col = get_column(board, i)
            col = make_move_on_list(col)
            put_column(board, col, i)
    if cmd == 's':
        cols = []
        for i in range(4):
            col = get_column(board, i)
            col.reverse()
            col = make_move_on_list(col)
            col.reverse()
            put_column(board, col, i)
    if cmd == 'a':
        row = []
        for i in range(4):
            row = get_row(board, i)
            row = make_move_on_list(row)
            put_row(board, row, i)
    if cmd == 'd':
        row = []
        for i in range(4):
            row = get_row(board, i)
            row.reverse()
            row = make_move_on_list(row)
            row.reverse()
            put_row(board, row, i)

#
# Problem 3.5
#

def game_over(board):
    '''
    Return True if the game is over i.e. if no moves can be made on the board.
    The board is not altered.

    Argument: board -- the game board
    Return value: True if the game is over, else False
    '''
    for i in ['w', 's', 'a', 'd']:
        board2 = board.copy()
        make_move(board2, i)
        if board != board2:
            return False
    return True

#
# Problem 3.6
#

def update(board, cmd):
    '''
    Make a move on a board given a movement command.  If the board has changed,
    then add a new number (1, 2 or 3, equal probability) on an empty edge square
    on the opposite side of the board to the move. (So if the move was to the
    left, add a number to an empty square on the right edge of the board.) If
    there is more than one empty edge square that can be filled, choose one at
    random.

    This function assumes that a move can be made on the board.

    Arguments:
      board  -- the game board
      cmd    -- the command letter

    Return value: none; the board is updated in-place.
    '''
    pos = []
    old = board.copy()
    make_move(board, cmd)
    for i in opposite_edge(cmd):
        if i not in board:
            pos.append(i)
    if board != old:
        board[random.choice(pos)] = random.randint(1, 3)


#
# Supplied to students:
#

def opposite_edge(cmd):
    '''
    Given a movement command, return the locations of squares which are
    eligible to be filled with a new number.

    Argument: cmd: one letter ('w', 's', 'a', or 'd')
    Return value: a list of (row, column) locations
    '''

    if cmd == 'w':    # up
        return [(3, 0), (3, 1), (3, 2), (3, 3)]  # bottom edge
    elif cmd == 's':  # down
        return [(0, 0), (0, 1), (0, 2), (0, 3)]  # top edge
    elif cmd == 'a':  # left
        return [(0, 3), (1, 3), (2, 3), (3, 3)]  # right edge
    elif cmd == 'd':  # right
        return [(0, 0), (1, 0), (2, 0), (3, 0)]  # left edge

def display(board):
    '''
    Display the board on the terminal in a human-readable form.

    Arguments:
      board  -- the game board

    Return value: none
    '''

    s1 = '+------+------+------+------+'
    s2 = '| {:^4s} | {:^4s} | {:^4s} | {:^4s} |'

    print(s1)
    for row in range(4):
        c0 = str(board.get((row, 0), ''))
        c1 = str(board.get((row, 1), ''))
        c2 = str(board.get((row, 2), ''))
        c3 = str(board.get((row, 3), ''))
        print(s2.format(c0, c1, c2, c3))
        print(s1)

def play_game():
    '''
    Play a game interactively.  Stop when the board is completely full
    and no moves can be made.

    Arguments: none
    Return value: none
    '''

    b = make_board()
    display(b)
    while True:
        if game_over(b):
            print('Game over!')
            break

        move = input('Enter move: ')
        if move not in ['w', 'a', 's', 'd', 'q']:
            print("Invalid move!  Only 'w', 'a', 's', 'd' or 'q' allowed.")
            print('Try again.')
            continue
        if move == 'q':  # quit
            return
        update(b, move)
        display(b)


#
# Useful for testing:
#

def list_to_board(lst):
    '''
    Convert a length-16 list into a board.
    '''
    board = {}
    k = 0
    for i in range(4):
        for j in range(4):
            if lst[k] != 0:
                board[(i, j)] = lst[k]
            k += 1
    return board

def random_game():
    '''Play a random game.'''
    board = make_board()
    display(board)
    while True:
        print()
        move = random.choice('wasd')
        update(board, move)
        display(board)
        if game_over(board):
            break
