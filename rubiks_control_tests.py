import copy
import random as r
import traceback as tb
import rubiks_control as c
import rubiks_cube as cc
import rubiks_utils as u

NTESTS = 100

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

# ---------------------------------------------------------------------- 
# Tests.
# ---------------------------------------------------------------------- 

def test_do_add_command():
    for size in [2, 3]:
        control = c.RubiksControl(size)
        cmds = copy.deepcopy(control.user_commands)
        control.do_add_command('foobar', ['baz'])
        cmds2 = control.user_commands
        assert len(cmds2) == len(cmds) + 1
        assert cmds2['foobar'] == 'baz'
   
    for size in [2, 3]:
        control = c.RubiksControl(size)
        cmds = copy.deepcopy(control.user_commands)
        control.do_add_command('xyzzy', ['foo', 'bar', 'baz'])
        cmds2 = control.user_commands
        assert len(cmds2) == len(cmds) + 1
        assert cmds2['xyzzy'] == 'foo bar baz'
   
def test_do_command():
    for size in [2, 3]:
        control = c.RubiksControl(size)
        cube = cc.RubiksCube(size)

        # Use test data, as usual.
        control.cube.rep.test_faces()
        cube.rep.test_faces()

        control.do_command('f')
        cube.move_face('F', '+')
        assert control.cube.rep.contents == cube.rep.contents

        control.do_command("u'")
        cube.move_face('U', '-')
        assert control.cube.rep.contents == cube.rep.contents

        control.do_command('fur')  # == f u r u' r' f'
        cube.move_face('F', '+')
        cube.move_face('U', '+')
        cube.move_face('R', '+')
        cube.move_face('U', '-')
        cube.move_face('R', '-')
        cube.move_face('F', '-')
        assert control.cube.rep.contents == cube.rep.contents

        # Check that bogus moves raise a BadCommand exception.
        try:
            control.do_command('foobarbazbam')
            print('ERROR: a BadCommand exception should have been raised')
            assert False
        except c.BadCommand:
            pass
        except:
            print('ERROR: a BadCommand exception should have been raised ', end='')
            print('       but a different exception was raised instead.')
            assert False


# ---------------------------------------------------------------------- 
# Entry point.
# ---------------------------------------------------------------------- 

if __name__ == '__main__':
    reset_test_counts()

    tests = [
      test_do_add_command,
      test_do_command,
    ]

    print()
    for test in tests:
        run_test(test)
    print()
    wrap_up()

