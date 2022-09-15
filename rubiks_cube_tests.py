import copy
import random as r
import traceback as tb
import rubiks_cube as c
import rubiks_utils as u

NTESTS = 100

class TestError(Exception):
    pass

# ---------------------------------------------------------------------- 
# Test framework.
# ---------------------------------------------------------------------- 

# Global variables.
ntests = 0
test_failures = 0
test_successes = 0

def reset_test_counts():
    '''
    Reset the test counter variables to 0.
    '''

    global ntests, test_failures, test_successes
    ntests = 0
    test_failures = 0
    test_successes = 0

def run_test(testfunc):
    '''
    Run a test.  Catch and display any tracebacks.
    Update test statistics.

    Arguments:
      testfunc -- the test function

    Return value: none

    Side effects:
      The global variables 'ntests', 'test_failures', and 'test_successes'
      may be updated.
    '''

    global ntests, test_failures, test_successes
    print('{} ... '.format(testfunc.__name__), end='')
    ntests += 1
    try:
        testfunc()
    except AssertionError as e:
        traceback_str = ''.join(tb.format_tb(e.__traceback__))
        print()
        print('-' * 70)
        print(traceback_str.strip())
        print('-' * 70)
        test_failures += 1
        print('test failed\n')
        return
    test_successes += 1
    print('passed')

def wrap_up():
    '''Print overall test results.'''
    print(f'Number of tests:  {ntests:4}')
    print(f'Tests passed:     {test_successes:4}')
    print(f'Tests failed:     {test_failures:4}')
    print()

def check_equal(expected, actual, err_msg):
    '''
    Check if an expected value equals an actual value.
    If so, return True.
    If not, print an error message and return False.
    '''
    if expected != actual:
        print(f'\nERROR: {err_msg}')
        print(f'  Expected: {expected}')
        print(f'  Got: {actual}')
        return False
    return True

def check(expr):
    try:
        expr()
        return True
    except TestError as e:
        print(e)
        return False

# ---------------------------------------------------------------------- 
# Helper data.
# ---------------------------------------------------------------------- 

#
# 2x2 cube, test data, before and after face rotations.
#

cube2_orig = {'U': [['a', 'b'], ['c', 'd']], 'D': [['e', 'f'], ['g', 'h']], 'F': [['i', 'j'], ['k', 'l']], 'B': [['m', 'n'], ['o', 'p']], 'L': [['q', 'r'], ['s', 't']], 'R': [['u', 'v'], ['w', 'x']]}

cube2_u_plus = {'U': [['c', 'a'], ['d', 'b']], 'D': [['e', 'f'], ['g', 'h']], 'F': [['u', 'v'], ['k', 'l']], 'B': [['m', 'n'], ['r', 'q']], 'L': [['i', 'j'], ['s', 't']], 'R': [['p', 'o'], ['w', 'x']]}

cube2_u_minus = {'U': [['b', 'd'], ['a', 'c']], 'D': [['e', 'f'], ['g', 'h']], 'F': [['q', 'r'], ['k', 'l']], 'B': [['m', 'n'], ['v', 'u']], 'L': [['p', 'o'], ['s', 't']], 'R': [['i', 'j'], ['w', 'x']]}

cube2_d_plus = {'U': [['a', 'b'], ['c', 'd']], 'D': [['g', 'e'], ['h', 'f']], 'F': [['i', 'j'], ['s', 't']], 'B': [['x', 'w'], ['o', 'p']], 'L': [['q', 'r'], ['n', 'm']], 'R': [['u', 'v'], ['k', 'l']]}

cube2_d_minus = {'U': [['a', 'b'], ['c', 'd']], 'D': [['f', 'h'], ['e', 'g']], 'F': [['i', 'j'], ['w', 'x']], 'B': [['t', 's'], ['o', 'p']], 'L': [['q', 'r'], ['k', 'l']], 'R': [['u', 'v'], ['n', 'm']]}

cube2_f_plus = {'U': [['a', 'b'], ['t', 'r']], 'D': [['w', 'u'], ['g', 'h']], 'F': [['k', 'i'], ['l', 'j']], 'B': [['m', 'n'], ['o', 'p']], 'L': [['q', 'e'], ['s', 'f']], 'R': [['c', 'v'], ['d', 'x']]}

cube2_f_minus = {'U': [['a', 'b'], ['u', 'w']], 'D': [['r', 't'], ['g', 'h']], 'F': [['j', 'l'], ['i', 'k']], 'B': [['m', 'n'], ['o', 'p']], 'L': [['q', 'd'], ['s', 'c']], 'R': [['f', 'v'], ['e', 'x']]}

cube2_b_plus = {'U': [['v', 'x'], ['c', 'd']], 'D': [['e', 'f'], ['q', 's']], 'F': [['i', 'j'], ['k', 'l']], 'B': [['o', 'm'], ['p', 'n']], 'L': [['b', 'r'], ['a', 't']], 'R': [['u', 'h'], ['w', 'g']]}

cube2_b_minus = {'U': [['s', 'q'], ['c', 'd']], 'D': [['e', 'f'], ['x', 'v']], 'F': [['i', 'j'], ['k', 'l']], 'B': [['n', 'p'], ['m', 'o']], 'L': [['g', 'r'], ['h', 't']], 'R': [['u', 'a'], ['w', 'b']]}

cube2_l_plus = {'U': [['m', 'b'], ['o', 'd']], 'D': [['i', 'f'], ['k', 'h']], 'F': [['a', 'j'], ['c', 'l']], 'B': [['e', 'n'], ['g', 'p']], 'L': [['s', 'q'], ['t', 'r']], 'R': [['u', 'v'], ['w', 'x']]}

cube2_l_minus = {'U': [['i', 'b'], ['k', 'd']], 'D': [['m', 'f'], ['o', 'h']], 'F': [['e', 'j'], ['g', 'l']], 'B': [['a', 'n'], ['c', 'p']], 'L': [['r', 't'], ['q', 's']], 'R': [['u', 'v'], ['w', 'x']]}

cube2_r_plus = {'U': [['a', 'j'], ['c', 'l']], 'D': [['e', 'n'], ['g', 'p']], 'F': [['i', 'f'], ['k', 'h']], 'B': [['m', 'b'], ['o', 'd']], 'L': [['q', 'r'], ['s', 't']], 'R': [['w', 'u'], ['x', 'v']]}

cube2_r_minus = {'U': [['a', 'n'], ['c', 'p']], 'D': [['e', 'j'], ['g', 'l']], 'F': [['i', 'b'], ['k', 'd']], 'B': [['m', 'f'], ['o', 'h']], 'L': [['q', 'r'], ['s', 't']], 'R': [['v', 'x'], ['u', 'w']]}

#
# 3x3 cube, test data, before and after face rotations.
#

cube3_orig = {'U': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'D': [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'F': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'B': [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'L': [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']], 'R': [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]}

cube3_u_plus = {'U': [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']], 'D': [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'F': [['T', 'U', 'V'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'B': [['B', 'C', 'D'], ['E', 'F', 'G'], ['M', 'L', 'K']], 'L': [['s', 't', 'u'], ['N', 'O', 'P'], ['Q', 'R', 'S']], 'R': [['J', 'I', 'H'], ['W', 'X', 'Y'], ['Z', '@', '#']]}

cube3_u_minus = {'U': [['c', 'f', 'i'], ['b', 'e', 'h'], ['a', 'd', 'g']], 'D': [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'F': [['K', 'L', 'M'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'B': [['B', 'C', 'D'], ['E', 'F', 'G'], ['V', 'U', 'T']], 'L': [['J', 'I', 'H'], ['N', 'O', 'P'], ['Q', 'R', 'S']], 'R': [['s', 't', 'u'], ['W', 'X', 'Y'], ['Z', '@', '#']]}

cube3_d_plus = {'U': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'D': [['p', 'm', 'j'], ['q', 'n', 'k'], ['r', 'o', 'l']], 'F': [['s', 't', 'u'], ['v', 'w', 'x'], ['Q', 'R', 'S']], 'B': [['#', '@', 'Z'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'L': [['K', 'L', 'M'], ['N', 'O', 'P'], ['D', 'C', 'B']], 'R': [['T', 'U', 'V'], ['W', 'X', 'Y'], ['y', 'z', 'A']]}

cube3_d_minus = {'U': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'D': [['l', 'o', 'r'], ['k', 'n', 'q'], ['j', 'm', 'p']], 'F': [['s', 't', 'u'], ['v', 'w', 'x'], ['Z', '@', '#']], 'B': [['S', 'R', 'Q'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'L': [['K', 'L', 'M'], ['N', 'O', 'P'], ['y', 'z', 'A']], 'R': [['T', 'U', 'V'], ['W', 'X', 'Y'], ['D', 'C', 'B']]}

cube3_f_plus = {'U': [['a', 'b', 'c'], ['d', 'e', 'f'], ['S', 'P', 'M']], 'D': [['Z', 'W', 'T'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'F': [['y', 'v', 's'], ['z', 'w', 't'], ['A', 'x', 'u']], 'B': [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'L': [['K', 'L', 'j'], ['N', 'O', 'k'], ['Q', 'R', 'l']], 'R': [['g', 'U', 'V'], ['h', 'X', 'Y'], ['i', '@', '#']]}

cube3_f_minus = {'U': [['a', 'b', 'c'], ['d', 'e', 'f'], ['T', 'W', 'Z']], 'D': [['M', 'P', 'S'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'F': [['u', 'x', 'A'], ['t', 'w', 'z'], ['s', 'v', 'y']], 'B': [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'L': [['K', 'L', 'i'], ['N', 'O', 'h'], ['Q', 'R', 'g']], 'R': [['l', 'U', 'V'], ['k', 'X', 'Y'], ['j', '@', '#']]}

cube3_b_plus = {'U': [['V', 'Y', '#'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'D': [['j', 'k', 'l'], ['m', 'n', 'o'], ['K', 'N', 'Q']], 'F': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'B': [['H', 'E', 'B'], ['I', 'F', 'C'], ['J', 'G', 'D']], 'L': [['c', 'L', 'M'], ['b', 'O', 'P'], ['a', 'R', 'S']], 'R': [['T', 'U', 'r'], ['W', 'X', 'q'], ['Z', '@', 'p']]}

cube3_b_minus = {'U': [['Q', 'N', 'K'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'D': [['j', 'k', 'l'], ['m', 'n', 'o'], ['#', 'Y', 'V']], 'F': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'B': [['D', 'G', 'J'], ['C', 'F', 'I'], ['B', 'E', 'H']], 'L': [['p', 'L', 'M'], ['q', 'O', 'P'], ['r', 'R', 'S']], 'R': [['T', 'U', 'a'], ['W', 'X', 'b'], ['Z', '@', 'c']]}

cube3_l_plus = {'U': [['B', 'b', 'c'], ['E', 'e', 'f'], ['H', 'h', 'i']], 'D': [['s', 'k', 'l'], ['v', 'n', 'o'], ['y', 'q', 'r']], 'F': [['a', 't', 'u'], ['d', 'w', 'x'], ['g', 'z', 'A']], 'B': [['j', 'C', 'D'], ['m', 'F', 'G'], ['p', 'I', 'J']], 'L': [['Q', 'N', 'K'], ['R', 'O', 'L'], ['S', 'P', 'M']], 'R': [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]}

cube3_l_minus = {'U': [['s', 'b', 'c'], ['v', 'e', 'f'], ['y', 'h', 'i']], 'D': [['B', 'k', 'l'], ['E', 'n', 'o'], ['H', 'q', 'r']], 'F': [['j', 't', 'u'], ['m', 'w', 'x'], ['p', 'z', 'A']], 'B': [['a', 'C', 'D'], ['d', 'F', 'G'], ['g', 'I', 'J']], 'L': [['M', 'P', 'S'], ['L', 'O', 'R'], ['K', 'N', 'Q']], 'R': [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']]}

cube3_r_plus = {'U': [['a', 'b', 'u'], ['d', 'e', 'x'], ['g', 'h', 'A']], 'D': [['j', 'k', 'D'], ['m', 'n', 'G'], ['p', 'q', 'J']], 'F': [['s', 't', 'l'], ['v', 'w', 'o'], ['y', 'z', 'r']], 'B': [['B', 'C', 'c'], ['E', 'F', 'f'], ['H', 'I', 'i']], 'L': [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']], 'R': [['Z', 'W', 'T'], ['@', 'X', 'U'], ['#', 'Y', 'V']]}

cube3_r_minus = {'U': [['a', 'b', 'D'], ['d', 'e', 'G'], ['g', 'h', 'J']], 'D': [['j', 'k', 'u'], ['m', 'n', 'x'], ['p', 'q', 'A']], 'F': [['s', 't', 'c'], ['v', 'w', 'f'], ['y', 'z', 'i']], 'B': [['B', 'C', 'l'], ['E', 'F', 'o'], ['H', 'I', 'r']], 'L': [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']], 'R': [['V', 'Y', '#'], ['U', 'X', '@'], ['T', 'W', 'Z']]}

#
# 2x2 cube, test data, after cube rotations.
#

cube2_x_plus = {'U': [['i', 'j'], ['k', 'l']], 'D': [['m', 'n'], ['o', 'p']], 'F': [['e', 'f'], ['g', 'h']], 'B': [['a', 'b'], ['c', 'd']], 'L': [['r', 't'], ['q', 's']], 'R': [['w', 'u'], ['x', 'v']]}

cube2_x_minus = {'U': [['m', 'n'], ['o', 'p']], 'D': [['i', 'j'], ['k', 'l']], 'F': [['a', 'b'], ['c', 'd']], 'B': [['e', 'f'], ['g', 'h']], 'L': [['s', 'q'], ['t', 'r']], 'R': [['v', 'x'], ['u', 'w']]}

cube2_y_plus = {'U': [['c', 'a'], ['d', 'b']], 'D': [['f', 'h'], ['e', 'g']], 'F': [['u', 'v'], ['w', 'x']], 'B': [['t', 's'], ['r', 'q']], 'L': [['i', 'j'], ['k', 'l']], 'R': [['p', 'o'], ['n', 'm']]}

cube2_y_minus = {'U': [['b', 'd'], ['a', 'c']], 'D': [['g', 'e'], ['h', 'f']], 'F': [['q', 'r'], ['s', 't']], 'B': [['x', 'w'], ['v', 'u']], 'L': [['p', 'o'], ['n', 'm']], 'R': [['i', 'j'], ['k', 'l']]}

cube2_z_plus = {'U': [['s', 'q'], ['t', 'r']], 'D': [['w', 'u'], ['x', 'v']], 'F': [['k', 'i'], ['l', 'j']], 'B': [['n', 'p'], ['m', 'o']], 'L': [['g', 'e'], ['h', 'f']], 'R': [['c', 'a'], ['d', 'b']]}

cube2_z_minus = {'U': [['v', 'x'], ['u', 'w']], 'D': [['r', 't'], ['q', 's']], 'F': [['j', 'l'], ['i', 'k']], 'B': [['o', 'm'], ['p', 'n']], 'L': [['b', 'd'], ['a', 'c']], 'R': [['f', 'h'], ['e', 'g']]}

#
# 3x3 cube, test data, after cube rotations.
#

cube3_x_plus = {'U': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'D': [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'F': [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'B': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'L': [['M', 'P', 'S'], ['L', 'O', 'R'], ['K', 'N', 'Q']], 'R': [['Z', 'W', 'T'], ['@', 'X', 'U'], ['#', 'Y', 'V']]}

cube3_x_minus = {'U': [['B', 'C', 'D'], ['E', 'F', 'G'], ['H', 'I', 'J']], 'D': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'F': [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], 'B': [['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r']], 'L': [['Q', 'N', 'K'], ['R', 'O', 'L'], ['S', 'P', 'M']], 'R': [['V', 'Y', '#'], ['U', 'X', '@'], ['T', 'W', 'Z']]}

cube3_y_plus = {'U': [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']], 'D': [['l', 'o', 'r'], ['k', 'n', 'q'], ['j', 'm', 'p']], 'F': [['T', 'U', 'V'], ['W', 'X', 'Y'], ['Z', '@', '#']], 'B': [['S', 'R', 'Q'], ['P', 'O', 'N'], ['M', 'L', 'K']], 'L': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']], 'R': [['J', 'I', 'H'], ['G', 'F', 'E'], ['D', 'C', 'B']]}

cube3_y_minus = {'U': [['c', 'f', 'i'], ['b', 'e', 'h'], ['a', 'd', 'g']], 'D': [['p', 'm', 'j'], ['q', 'n', 'k'], ['r', 'o', 'l']], 'F': [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']], 'B': [['#', '@', 'Z'], ['Y', 'X', 'W'], ['V', 'U', 'T']], 'L': [['J', 'I', 'H'], ['G', 'F', 'E'], ['D', 'C', 'B']], 'R': [['s', 't', 'u'], ['v', 'w', 'x'], ['y', 'z', 'A']]}

cube3_z_plus = {'U': [['Q', 'N', 'K'], ['R', 'O', 'L'], ['S', 'P', 'M']], 'D': [['Z', 'W', 'T'], ['@', 'X', 'U'], ['#', 'Y', 'V']], 'F': [['y', 'v', 's'], ['z', 'w', 't'], ['A', 'x', 'u']], 'B': [['D', 'G', 'J'], ['C', 'F', 'I'], ['B', 'E', 'H']], 'L': [['p', 'm', 'j'], ['q', 'n', 'k'], ['r', 'o', 'l']], 'R': [['g', 'd', 'a'], ['h', 'e', 'b'], ['i', 'f', 'c']]}

cube3_z_minus = {'U': [['V', 'Y', '#'], ['U', 'X', '@'], ['T', 'W', 'Z']], 'D': [['M', 'P', 'S'], ['L', 'O', 'R'], ['K', 'N', 'Q']], 'F': [['u', 'x', 'A'], ['t', 'w', 'z'], ['s', 'v', 'y']], 'B': [['H', 'E', 'B'], ['I', 'F', 'C'], ['J', 'G', 'D']], 'L': [['c', 'f', 'i'], ['b', 'e', 'h'], ['a', 'd', 'g']], 'R': [['l', 'o', 'r'], ['k', 'n', 'q'], ['j', 'm', 'p']]}

# ---------------------------------------------------------------------- 
# Helper functions.
# ---------------------------------------------------------------------- 

def validate_cube_lite(cube, size):
    '''
    Check if a cube representation is valid.
    NOTE: Doesn't check colors.
    NOTE: Doesn't check for parity errors.
    '''

    # Check that the cube is a dictionary.
    if type(cube) is not dict:
        print(f'cube: {cube}')
        raise TestError('cube is not a dictionary')

    # Check that there are exactly six keys: 'U', 'D', 'F', 'B', 'L' and 'R'.
    if set(cube.keys()) != { 'U', 'D', 'F', 'B', 'L', 'R' }:
        print(f'cube: {cube}')
        raise TestError('cube does not have the correct keys: U D F B L R')

    # Check that all values are size*size lists of lists.
    for (key, val) in cube.items():
        if type(val) is not list:
            print(f'key: {key}; value: {val}')
            raise TestError('cube value is not a list')
        if len(val) != size:
            print(f'key: {key}; value: {val}')
            msg = f'cube value does not have the right length: {size}'
            raise TestError(msg)
        for item in val:
            if type(item) is not list:
                print(f'key: {key}; value: {val}')
                raise TestError(f'cube value is not a list of lists')
            if len(item) != size:
                print(f'key: {key}; value: {val}')
                msg = f'value sublist does not have the right length: {size}'
                raise TestError(msg)

    # Check for aliasing.
    for val in cube.values():
        for i in range(size):
            for j in range(i + 1, size):
                if val[i] is val[j]:   # identity checking
                    msg = f'val {val}: sublists {i} and {j} are aliases'
                    return TestError(msg)

# ---------------------------------------------------------------------- 
# Tests.
# ---------------------------------------------------------------------- 

def test_rotate_cube():
    #
    # Size = 2
    #

    cube = c.RubiksCube(2)
    cube.rep.test_faces()
    contents = copy.deepcopy(cube.rep.contents)
    assert cube.rep.contents == cube2_orig

    count = cube.count
    cube.rotate_cube('X', '+')
    assert cube.rep.contents == cube2_x_plus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('X', '-')
    assert cube.rep.contents == cube2_x_minus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Y', '+')
    assert cube.rep.contents == cube2_y_plus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Y', '-')
    assert cube.rep.contents == cube2_y_minus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Z', '+')
    assert cube.rep.contents == cube2_z_plus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Z', '-')
    assert cube.rep.contents == cube2_z_minus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    #
    # Size = 3
    #

    cube = c.RubiksCube(3)
    cube.rep.test_faces()
    contents = copy.deepcopy(cube.rep.contents)
    assert cube.rep.contents == cube3_orig

    count = cube.count
    cube.rotate_cube('X', '+')
    assert cube.rep.contents == cube3_x_plus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('X', '-')
    assert cube.rep.contents == cube3_x_minus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Y', '+')
    assert cube.rep.contents == cube3_y_plus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Y', '-')
    assert cube.rep.contents == cube3_y_minus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Z', '+')
    assert cube.rep.contents == cube3_z_plus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.rotate_cube('Z', '-')
    assert cube.rep.contents == cube3_z_minus
    assert cube.count == count  # no change
    cube.rep.contents = copy.deepcopy(contents)

def test_move_face():
    #
    # Size = 2
    #

    cube = c.RubiksCube(2)
    cube.rep.test_faces()
    contents = copy.deepcopy(cube.rep.contents)
    assert cube.rep.contents == cube2_orig

    count = cube.count
    cube.move_face('U', '+')
    assert cube.rep.contents == cube2_u_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('U', '-')
    assert cube.rep.contents == cube2_u_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('D', '+')
    assert cube.rep.contents == cube2_d_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('D', '-')
    assert cube.rep.contents == cube2_d_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('F', '+')
    assert cube.rep.contents == cube2_f_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('F', '-')
    assert cube.rep.contents == cube2_f_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('B', '+')
    assert cube.rep.contents == cube2_b_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('B', '-')
    assert cube.rep.contents == cube2_b_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('L', '+')
    assert cube.rep.contents == cube2_l_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('L', '-')
    assert cube.rep.contents == cube2_l_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('R', '+')
    assert cube.rep.contents == cube2_r_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('R', '-')
    assert cube.rep.contents == cube2_r_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    #
    # Size = 3
    #

    cube = c.RubiksCube(3)
    cube.rep.test_faces()
    contents = copy.deepcopy(cube.rep.contents)
    assert cube.rep.contents == cube3_orig

    count = cube.count
    cube.move_face('U', '+')
    assert cube.rep.contents == cube3_u_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('U', '-')
    assert cube.rep.contents == cube3_u_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('D', '+')
    assert cube.rep.contents == cube3_d_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('D', '-')
    assert cube.rep.contents == cube3_d_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('F', '+')
    assert cube.rep.contents == cube3_f_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('F', '-')
    assert cube.rep.contents == cube3_f_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('B', '+')
    assert cube.rep.contents == cube3_b_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('B', '-')
    assert cube.rep.contents == cube3_b_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('L', '+')
    assert cube.rep.contents == cube3_l_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('L', '-')
    assert cube.rep.contents == cube3_l_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('R', '+')
    assert cube.rep.contents == cube3_r_plus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

    count = cube.count
    cube.move_face('R', '-')
    assert cube.rep.contents == cube3_r_minus
    assert cube.count == count + 1
    cube.rep.contents = copy.deepcopy(contents)

def test_is_solved():
    # Test that solved cubes are solved :)
    cube = c.RubiksCube(2)
    assert cube.is_solved()
    cube = c.RubiksCube(3)
    assert cube.is_solved()

    # Test that scrambled cubes are not solved.
    # There is a vanishingly small probability that this test will fail
    # due to a scramble which does nothing.
    cube = c.RubiksCube(2)
    cube.scramble()
    assert not cube.is_solved()
    cube = c.RubiksCube(3)
    cube.scramble()
    assert not cube.is_solved()

    # Test that cubes containing only one color are not solved.
    face_contents2 = [['w', 'w'], ['w', 'w']]
    rep2 = {}
    for face in 'UDFBLR':
        rep2[face] = copy.deepcopy(face_contents2)
    cube = c.RubiksCube(2)
    cube.rep.contents = rep2
    try:
        cube.is_solved()
        assert False  # should never reach here!
    except c.InvalidCube as e:
        pass
    except:   # all other exceptions are mistakes.
        print('Expecting InvalidCube exception')
        assert False

    face_contents3 = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    rep3 = {}
    for face in 'UDFBLR':
        rep3[face] = copy.deepcopy(face_contents3)
    cube = c.RubiksCube(3)
    cube.rep.contents = rep3
    try:
        cube.is_solved()
        assert False  # should never reach here!
    except c.InvalidCube as e:
        pass
    except:   # all other exceptions are mistakes.
        print('Expecting InvalidCube exception')
        assert False

    # Test that cubes containing all the one-color faces 
    # in an invalid orientation are not solved.
    for size in [2, 3]:
        cube = c.RubiksCube(size)
        contents = cube.rep.contents
        (U, F) = (contents['U'], contents['F'])
        contents['U'] = F
        contents['F'] = U
        cube.rep.contents = contents
        try:
            cube.is_solved()
            assert False  # should never reach here!
        except c.InvalidCube as e:
            pass
        except:   # all other exceptions are mistakes.
            print('Expecting InvalidCube exception')
            assert False

    for size in [2, 3]:
        cube = c.RubiksCube(size)
        contents = cube.rep.contents
        (U, D) = (contents['U'], contents['D'])
        contents['U'] = D
        contents['D'] = U
        cube.rep.contents = contents
        try:
            cube.is_solved()
            assert False  # should never reach here!
        except c.InvalidCube as e:
            pass
        except:   # all other exceptions are mistakes.
            print('Expecting InvalidCube exception')
            assert False

# ---------------------------------------------------------------------- 
# Entry point.
# ---------------------------------------------------------------------- 

if __name__ == '__main__':
    reset_test_counts()

    tests = [
      test_rotate_cube,
      test_move_face,
      test_is_solved,
    ]

    print()
    for test in tests:
        run_test(test)
    print()
    wrap_up()

