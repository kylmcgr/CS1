import random, sys, copy
import midterm as m

#
# PART 2.
#

### 2.1

def test_draw_checkerboard():
    # Management apologizes for the long lines.
    cb11 = '\n+-+\n|#|\n+-+\n'
    cb12 = '\n+-+-+\n|#| |\n+-+-+\n'
    cb21 = '\n+-+\n| |\n+-+\n|#|\n+-+\n'
    cb22 = '\n+-+-+\n| |#|\n+-+-+\n|#| |\n+-+-+\n' 

    cb44 = '\n+-+-+-+-+\n| |#| |#|\n+-+-+-+-+\n|#| |#| |\n+-+-+-+-+\n| |#| |#|\n+-+-+-+-+\n|#| |#| |\n+-+-+-+-+\n'
    cb45 = '\n+-+-+-+-+-+\n| |#| |#| |\n+-+-+-+-+-+\n|#| |#| |#|\n+-+-+-+-+-+\n| |#| |#| |\n+-+-+-+-+-+\n|#| |#| |#|\n+-+-+-+-+-+\n'
    cb54 = '\n+-+-+-+-+\n|#| |#| |\n+-+-+-+-+\n| |#| |#|\n+-+-+-+-+\n|#| |#| |\n+-+-+-+-+\n| |#| |#|\n+-+-+-+-+\n|#| |#| |\n+-+-+-+-+\n'
    cb55 = '\n+-+-+-+-+-+\n|#| |#| |#|\n+-+-+-+-+-+\n| |#| |#| |\n+-+-+-+-+-+\n|#| |#| |#|\n+-+-+-+-+-+\n| |#| |#| |\n+-+-+-+-+-+\n|#| |#| |#|\n+-+-+-+-+-+\n'

    cb88 = '\n+-+-+-+-+-+-+-+-+\n| |#| |#| |#| |#|\n+-+-+-+-+-+-+-+-+\n|#| |#| |#| |#| |\n+-+-+-+-+-+-+-+-+\n| |#| |#| |#| |#|\n+-+-+-+-+-+-+-+-+\n|#| |#| |#| |#| |\n+-+-+-+-+-+-+-+-+\n| |#| |#| |#| |#|\n+-+-+-+-+-+-+-+-+\n|#| |#| |#| |#| |\n+-+-+-+-+-+-+-+-+\n| |#| |#| |#| |#|\n+-+-+-+-+-+-+-+-+\n|#| |#| |#| |#| |\n+-+-+-+-+-+-+-+-+\n'

    assert m.draw_checkerboard(1, 1) == cb11
    assert m.draw_checkerboard(1, 2) == cb12
    assert m.draw_checkerboard(2, 1) == cb21
    assert m.draw_checkerboard(2, 2) == cb22

    assert m.draw_checkerboard(4, 4) == cb44
    assert m.draw_checkerboard(4, 5) == cb45
    assert m.draw_checkerboard(5, 4) == cb54
    assert m.draw_checkerboard(5, 5) == cb55

    assert m.draw_checkerboard(8, 8) == cb88

### 2.2

def test_roll_count():
    assert m.roll_count([1, 1, 1, 1, 1]) == {1: 5}
    assert m.roll_count([2, 1, 5, 3, 4]) == {2: 1, 1: 1, 5: 1, 3: 1, 4: 1}
    assert m.roll_count([2, 2, 2, 3, 3]) == {2: 3, 3: 2}
    assert m.roll_count([1, 6, 6, 6, 6]) == {1: 1, 6: 4}
    assert m.roll_count([6, 1, 6, 6, 6]) == {6: 4, 1: 1}
    assert m.roll_count([6, 1, 6, 3, 6]) == {6: 3, 1: 1, 3: 1}
    assert m.roll_count([6, 1, 4, 3, 2]) == {6: 1, 1: 1, 4: 1, 3: 1, 2: 1}

def test_yahtzee_classify():
    category = {
      'c'  : 'CHANCE',
      't'  : 'THREE OF A KIND',
      'f'  : 'FOUR OF A KIND',
      'fh' : 'FULL HOUSE',
      'ss' : 'SMALL STRAIGHT',
      'ls' : 'LARGE STRAIGHT',
      'y'  : 'YAHTZEE'
    }
      
    assert m.yahtzee_classify([1, 1, 1, 1, 1]) == category['y']
    assert m.yahtzee_classify([4, 4, 4, 4, 4]) == category['y']

    assert m.yahtzee_classify([4, 4, 4, 4, 1]) == category['f']
    assert m.yahtzee_classify([4, 1, 4, 4, 4]) == category['f']
    assert m.yahtzee_classify([2, 2, 3, 2, 2]) == category['f']

    assert m.yahtzee_classify([2, 2, 2, 4, 4]) == category['fh']
    assert m.yahtzee_classify([4, 2, 4, 2, 4]) == category['fh']

    assert m.yahtzee_classify([1, 2, 3, 4, 5]) == category['ls']
    assert m.yahtzee_classify([5, 2, 1, 4, 3]) == category['ls']
    assert m.yahtzee_classify([6, 2, 5, 4, 3]) == category['ls']

    assert m.yahtzee_classify([1, 3, 4, 5, 6]) == category['ss']
    assert m.yahtzee_classify([6, 1, 5, 4, 3]) == category['ss']
    assert m.yahtzee_classify([2, 3, 4, 5, 2]) == category['ss']
    assert m.yahtzee_classify([3, 4, 2, 2, 5]) == category['ss']
    assert m.yahtzee_classify([4, 1, 2, 3, 4]) == category['ss']
    assert m.yahtzee_classify([4, 2, 3, 4, 1]) == category['ss']

    assert m.yahtzee_classify([4, 4, 4, 1, 2]) == category['t']
    assert m.yahtzee_classify([1, 4, 2, 4, 4]) == category['t']
    assert m.yahtzee_classify([1, 4, 1, 6, 1]) == category['t']

    assert m.yahtzee_classify([1, 2, 2, 4, 6]) == category['c']
    assert m.yahtzee_classify([2, 2, 5, 4, 5]) == category['c']
    assert m.yahtzee_classify([2, 2, 1, 4, 5]) == category['c']



### 2.3

def test_nim_done():
    assert m.nim_done([]) == True
    assert m.nim_done([0]) == True
    assert m.nim_done([0, 0]) == True
    assert m.nim_done([0, 0, 0]) == True
    assert m.nim_done([5]) == False
    assert m.nim_done([0, 4]) == False
    assert m.nim_done([1, 0]) == False
    assert m.nim_done([1, 4]) == False
    assert m.nim_done([1, 4, 2]) == False
    assert m.nim_done([0, 4, 10]) == False
    assert m.nim_done([1, 5, 0]) == False
    assert m.nim_done([1, 0, 2]) == False
    assert m.nim_done([11, 5, 12]) == False

def test_nim_sum():
    assert m.nim_sum([]) == 0
    assert m.nim_sum([0]) == 0
    assert m.nim_sum([0, 0]) == 0
    assert m.nim_sum([0, 0, 0]) == 0
    assert m.nim_sum([5]) == 5
    assert m.nim_sum([0, 4]) == 4
    assert m.nim_sum([1, 0]) == 1
    assert m.nim_sum([1, 4]) == 5
    assert m.nim_sum([1, 4, 2]) == 7
    assert m.nim_sum([0, 4, 10]) == 14 
    assert m.nim_sum([1, 5, 0]) == 4
    assert m.nim_sum([1, 0, 2]) == 3
    assert m.nim_sum([11, 5, 12]) == 2
    assert m.nim_sum([11, 7, 12]) == 0

def test_nim_random_move():
    # Cases where there is only one move:
    assert m.nim_random_move([1]) == (0, 1)
    assert m.nim_random_move([1, 0]) == (0, 1)
    assert m.nim_random_move([0, 1]) == (1, 1)
    assert m.nim_random_move([0, 0, 0, 1, 0]) == (3, 1)

    # Cases where there is only one nonempty slot:
    for _ in range(100):
        (i, n) = m.nim_random_move([0, 0, 5, 0])
        assert i == 2
        assert n >= 1 and n <= 5

    # Other cases:
    for _ in range(100):
        a = random.randrange(5)
        b = random.randrange(5) + 1   # at least one valid move
        c = random.randrange(5)
        d = random.randrange(5)
        lst = [a, b, c, d]
        (i, n) = m.nim_random_move(lst)
        assert i >= 0
        assert i < 4
        assert lst[i] >= n

def test_nim_best_move():
    # Only meaningful if there is a unique best move.
    assert m.nim_best_move([1]) == (0, 1)
    assert m.nim_best_move([1, 0, 0]) == (0, 1)
    assert m.nim_best_move([0, 1, 0]) == (1, 1)
    assert m.nim_best_move([0, 10, 0]) == (1, 10)
    assert m.nim_best_move([3, 2, 0]) == (0, 1)
    assert m.nim_best_move([5, 3, 2]) == (0, 4)
    assert m.nim_best_move([5, 3]) == (0, 2)

#
# PART 3.
#

def test_make_board():
    for i in range(100):
        b = m.make_board()
        assert type(b) is dict  # make_board() returns a dictionary
        assert len(b) == 9
        n1 = 0
        n2 = 0
        n3 = 0
        for key in b:
            assert type(key) is tuple
            assert len(key) == 2
            (row, col) = key
            assert 0 <= row <= 3
            assert 0 <= col <= 3
            assert b[key] in [1, 2, 3]
            if b[key] == 1:
                n1 += 1
            elif b[key] == 2:
                n2 += 1
            elif b[key] == 3:
                n3 += 1
        assert n1 >= 1
        assert n2 >= 1
        assert n3 >= 1

def random_board():
    '''Create and return a random board.'''
    board = m.make_board()
    for i in range(100):
        move = random.choice('wasd')
        m.update(board, move)
        if m.game_over(board):
            break
    return board

def test_accessors():
    b = random_board()
    r0 = m.get_row(b, 0)
    r1 = m.get_row(b, 1)
    r2 = m.get_row(b, 2)
    r3 = m.get_row(b, 3)
    c0 = m.get_column(b, 0)
    c1 = m.get_column(b, 1)
    c2 = m.get_column(b, 2)
    c3 = m.get_column(b, 3)
    for item in [r0, r1, r2, r3, c0, c1, c2, c3]:
        assert type(item) is list
        assert len(item) == 4
        for elem in item:
            assert type(elem) is int
    m.put_row(b, [1, 2, 3, 6], 0)
    assert m.get_row(b, 0) == [1, 2, 3, 6]
    m.put_column(b, [3, 0, 0, 2], 2)
    assert m.get_column(b, 2) == [3, 0, 0, 2]
    assert (1, 2) not in b  # setting to 0 clears location
    assert (2, 2) not in b

def test_can_merge():
    assert m.can_merge(1, 2)
    assert m.can_merge(2, 1)
    assert m.can_merge(3, 3)
    assert m.can_merge(6, 6)
    assert not m.can_merge(1, 1)
    assert not m.can_merge(2, 2)
    assert not m.can_merge(3, 1)
    assert not m.can_merge(2, 3)
    assert not m.can_merge(3, 6)

def test_make_move_on_list():
    assert m.make_move_on_list([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert m.make_move_on_list([0, 2, 1, 0]) == [2, 1, 0, 0]
    assert m.make_move_on_list([0, 3, 0, 6]) == [3, 0, 6, 0]
    assert m.make_move_on_list([6, 6, 2, 2]) == [12, 2, 2, 0]
    assert m.make_move_on_list([2, 1, 2, 2]) == [3, 2, 2, 0]
    assert m.make_move_on_list([2, 2, 2, 2]) == [2, 2, 2, 2]
    assert m.make_move_on_list([2, 2, 3, 3]) == [2, 2, 6, 0]
    assert m.make_move_on_list([2, 6, 6, 0]) == [2, 12, 0, 0]
    assert m.make_move_on_list([2, 1, 2, 1]) == [3, 2, 1, 0]
    assert m.make_move_on_list([2, 0, 2, 1]) == [2, 2, 1, 0]
    assert m.make_move_on_list([0, 0, 0, 6]) == [0, 0, 6, 0]
    assert m.make_move_on_list([2, 0, 0, 3]) == [2, 0, 3, 0]
    assert m.make_move_on_list([2, 0, 6, 0]) == [2, 6, 0, 0]
    assert m.make_move_on_list([2, 6, 0, 0]) == [2, 6, 0, 0]
    assert m.make_move_on_list([3, 3, 0, 1]) == [6, 0, 1, 0]

def test_make_move():
    b = {(3, 2): 2, (2, 3): 2}
    m.make_move(b, 'w')
    assert b == {(2, 2): 2, (1, 3): 2}
    b = {(3, 2): 2, (2, 3): 2}
    m.make_move(b, 'd')
    assert b == {(3, 3): 2, (2, 3): 2}
    b = {(3, 2): 2, (2, 3): 2}
    m.make_move(b, 'a')
    assert b == {(3, 1): 2, (2, 2): 2} 
    b = {(3, 2): 2, (2, 3): 2}
    m.make_move(b, 's')
    assert b == {(3, 2): 2, (3, 3): 2} 
    m.make_move(b, 'a')
    assert b == {(3, 1): 2, (3, 2): 2} 

def test_game_over():
    b = m.make_board()
    assert not m.game_over(b)
    b = {(0, 0): 2, (0, 1): 3, (0, 2): 1, (0, 3): 3, 
         (1, 0): 3, (1, 1): 2, (1, 2): 6, (1, 3): 2, 
         (2, 0): 2, (2, 1): 3, (2, 2): 2, (2, 3): 12, 
         (3, 0): 3, (3, 1): 1, (3, 2): 12, (3, 3): 1}
    assert m.game_over(b)

def test_update():
    for i in range(100):
        b = m.make_board()
        for c in 'wasd':
            b2 = b.copy()
            m.make_move(b, c)
            m.update(b2, c)
            if b != b2:               # if a number was added ...
                for loc in b:
                    del b2[loc]
                assert len(b2) == 1   # make sure it's only one number...
                assert list(b2.values())[0] in [1, 2, 3]   # either 1, 2, or 3

if __name__ == '__main__':

    # Part 2.
    test_draw_checkerboard()

    test_roll_count()
    test_yahtzee_classify()

    test_nim_done()
    test_nim_sum()
    test_nim_random_move()
    test_nim_best_move()

    # Part 3.
    test_make_board()
    test_accessors()
    test_can_merge()
    test_make_move_on_list()
    test_make_move()
    test_game_over()
    test_update()

    print('All tests passed!')

