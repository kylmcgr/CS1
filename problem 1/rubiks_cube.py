# Name: Kyle McGraw
# Login: kmcgraw
'''
Rubik's cube class.
'''

import copy, random
import rubiks_utils as u
import rubiks_rep as r

class InvalidCube(Exception):
    '''
    This exception is raised when a cube has been determined to be in
    an invalid configuration.
    '''
    pass

class RubiksCube:
    '''
    This class implements all Rubik's cube operations.
    '''

    def __init__(self, size):
        '''Initialize the cube representation.'''
        # Cube representation.
        self.rep = r.RubiksRep(size)
        # Number of moves, quarter-turn metric.
        self.count = 0

    def get_state(self):
        '''
        Return a copy of the internal state of this object.
        '''
        rep = copy.deepcopy(self.rep)
        return (rep, self.count)

    def put_state(self, rep, count):
        '''
        Restore a previous state.
        '''
        self.rep = rep
        self.count = count

    ### Basic operations.

    def rotate_cube(self, axis, dir):
        '''
        Rotate the cube as a whole.
        The X axis means in the direction of an R turn.
        The Y axis means in the direction of a U turn.
        The Z axis means in the direction of an F turn.
        The + direction is clockwise.
        The - direction is counterclockwise.

        Arguments:
          axis -- one of ['X', 'Y', 'Z']
          dir  -- one of ['+', '-']

        Return value: none
        '''
        assert axis in ['X', 'Y', 'Z']
        assert dir in ['+', '-']
        dic2 = {'+' : 1, '-' : 3}
        for i in range(dic2[dir]):
            getattr(self.rep, 'rotate_cube_' + axis)()

    def move_slice(self, slice, dir):
        '''
        Move the specified slice.
        Arguments:
          -- slice: one of ['u', 'd', 'f', 'b', 'l', 'r']
          -- dir: '+' for clockwise or '-' for counterclockwise

        Return value: none
        '''
        assert slice in ['u', 'd', 'f', 'b', 'l', 'r', 'M', 'E', 'S']
        if self.rep.size % 2 == 0:
            assert slice in ['u', 'd', 'f', 'b', 'l', 'r']
        assert dir in ['+', '-']
        dic = {'u' : ['X', 3], 'd' : ['X', 1], 'f' : ['X', 0], 'b' : ['X', 2],
        'l' : ['Y', 3], 'r' : ['Y', 1], 'M' : ['Y', 3],
        'E' : ['X', 1], 'S' : ['X', 0]}
        dic2 = {'+' : 1, '-' : 3}
        for i in range(dic[slice][1]):
            self.rotate_cube(dic[slice][0], '+')
        for i in range(dic2[dir]):
            if slice in ['M', 'E', 'S']:
                self.rep.rotate_s()
            else:
                self.rep.rotate_f()
        for i in range(dic[slice][1]):
            self.rotate_cube(dic[slice][0], '-')
        self.count += 1

    def move_face(self, face, dir):
        '''
        Move the specified face.
        Arguments:
          -- face: one of ['U', 'D', 'L', 'R', 'F', 'B']
          -- dir: '+' for clockwise or '-' for counterclockwise

        Return value: none
        '''
        assert face in ['U', 'D', 'F', 'B', 'L', 'R']
        assert dir in ['+', '-']
        dic = {'U' : ['X', 3], 'D' : ['X', 1], 'F' : ['X', 0], 'B' : ['X', 2],
        'L' : ['Y', 3], 'R' : ['Y', 1]}
        dic2 = {'+' : 1, '-' : 3}
        for i in range(dic[face][1]):
            self.rotate_cube(dic[face][0], '+')
        for i in range(dic2[dir]):
            self.rep.move_F()
        for i in range(dic[face][1]):
            self.rotate_cube(dic[face][0], '-')
        self.count += 1

    def random_rotations(self, n):
        '''
        Rotate the entire cube randomly 'n' times.

        Arguments:
          n -- number of random rotations to make

        Return value: none
        '''
        for _ in range(n):
            rot = random.choice('XYZ')
            dir = random.choice('+-')
            self.rotate_cube(rot, dir)

    def random_moves(self, n):
        '''
        Make 'n' random moves.

        Arguments:
          n -- number of random moves to make

        Return value: none
        '''
        for _ in range(n):
            face = random.choice('UDFBLR')
            if self.rep.size > 3:
                face = random.choice('UDFBLRudfblr')
            dir  = random.choice('+-')
            if face in "udfblr":
                self.move_slice(face, dir)
            else:
                self.move_face(face, dir)

    def scramble(self, nrots=10, nmoves=50):
        '''
        Scramble the cube.

        Arguments:
          nrots  -- number of random cube rotations to make
          nmoves -- number of random face moves to make

        Return value: none
        '''

        self.random_rotations(nrots)
        self.random_moves(nmoves)
        # Reset count before solving begins.
        self.count = 0

    def is_solved(self):
        '''
        Return True if the cube is solved.

        If the cube appears solved but is invalid, raise an
        InvalidCube exception with an appropriate error message.
        '''
        faces = ['U', 'D', 'F', 'B', 'L', 'R']
        solved = ['b', 'g', 'o', 'r', 'w', 'y']
        opp = {'b' : 'g', 'g' : 'b', 'o' : 'r', 'r' : 'o', 'w' : 'y', 'y' : 'w'}
        corners = ['wgr', 'wrb', 'wbo', 'wog',
        'goy', 'gyr', 'grw', 'gwo',
        'ygo', 'yob', 'ybr', 'yrg',
        'rwg', 'rgy', 'ryb', 'rbw',
        'bwr', 'bry', 'byo', 'bow',
        'owb', 'oby', 'oyg', 'ogw']
        colors = []
        for i in range(len(faces)):
            color = self.rep.get_face(faces[i])[0][0]
            if i % 2 == 1 and colors[-1] != opp[color]:
                raise InvalidCube("Invalid cube: invalid opposite colors")
            if color not in solved or color in colors:
                raise InvalidCube("Invalid cube: invalid colors")
            for j in self.rep.get_face(faces[i]):
                for k in j:
                    if k != color:
                        return False
            if self.rep.get_face('U')[self.rep.size - 1][self.rep.size - 1] \
            + self.rep.get_face('F')[0][self.rep.size - 1] \
            + self.rep.get_face('R')[0][0] not in corners:
                raise InvalidCube("Invalid cube: invalid corners")
            colors.append(color)
        return True

    def display(self):
        '''
        Return a string version of the cube representation.
        '''
        return self.rep.display()

if __name__ == '__main__':
    cube = RubiksCube(3)
    print(cube.display())
    cube.scramble()
    print(cube.display())
