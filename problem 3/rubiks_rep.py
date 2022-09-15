# Name: Kyle McGraw
# Login: kmcgraw
'''
Rubik's cube representations and basic operations.
'''

import rubiks_utils as u
import copy

class RubiksRep:
    '''
    Basic functionality of Rubik's cubes.
    '''

    def __init__(self, size):
        '''
        Initialize the cube representation.
        '''
        assert size > 0
        self.size = size
        faces = ['U', 'D', 'F', 'B', 'L', 'R']
        color = ['w', 'y', 'r', 'o', 'g', 'b']
        self.contents = {}
        for i in range(len(faces)):
            self.contents[faces[i]] = []
            for j in range(size):
                self.contents[faces[i]].append([])
                for k in range(size):
                    self.contents[faces[i]][j].append(color[i])


    ### Accessors.

    def get_row(self, face, row):
        '''
        Return a copy of the indicated row on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert row >= 0 and row < self.size
        return self.contents[face][row].copy()

    def get_col(self, face, col):
        '''
        Return a copy of the indicated column on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert col >= 0 and col < self.size
        newcol = []
        for i in self.contents[face]:
            newcol.append(i[col])
        return newcol

    def set_row(self, face, row, values):
        '''
        Change the contents of the indicated row on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert row >= 0 and row < self.size
        assert type(values) is list
        assert len(values) == self.size
        self.contents[face][row] = values.copy()

    def set_col(self, face, col, values):
        '''
        Change the contents of the indicated column on the indicated face.
        The internal representation of the cube is not altered.
        '''
        assert face in self.contents
        assert col >= 0 and col < self.size
        assert type(values) is list
        assert len(values) == self.size
        for i in range(self.size):
            self.contents[face][i][col] = values[i]

    def get_face(self, face):
        '''
        Return the colors of a face, as a list of lists.
        '''
        assert face in self.contents
        return copy.deepcopy(self.contents[face])

    ### Basic operations.

    def rotate_face_cw(self, face):
        '''
        Rotate a face clockwise.
        '''
        assert face in self.contents
        new = []
        for i in range(self.size):
            new.append(self.get_row(face, i))
        for i in range(self.size):
            self.set_col(face, self.size - i - 1, new[i])

    def rotate_face_ccw(self, face):
        '''
        Rotate a face counterclockwise.
        '''
        assert face in self.contents
        new = []
        for i in range(self.size):
            new.append(self.get_col(face, self.size - i - 1))
        for i in range(self.size):
            self.set_row(face, i, new[i])

    def move_F(self):
        '''
        Move the F face one-quarter turn clockwise.
        '''
        self.rotate_face_cw('F')
        r = self.get_col('R', 0)
        l = self.get_col('L', self.size - 1)
        u = self.get_row('U', self.size - 1)
        d = self.get_row('D', 0)
        self.set_row('U', self.size - 1, l[::-1])
        self.set_row('D', 0, r[::-1])
        self.set_col('R', 0, u)
        self.set_col('L', self.size - 1, d)

    def rotate_cube_X(self):
        '''
        Rotate the cube in the positive X direction.
        '''
        self.rotate_face_cw('R')
        self.rotate_face_ccw('L')
        f = self.get_face('F')
        u = self.get_face('U')
        b = self.get_face('B')
        d = self.get_face('D')
        self.contents['U'] = f
        self.contents['B'] = u
        self.contents['D'] = b
        self.contents['F'] = d

    def rotate_cube_Y(self):
        '''
        Rotate the cube in the positive Y direction.
        '''
        self.rotate_face_cw('U')
        self.rotate_face_ccw('D')
        f = self.get_face('F')
        l = self.get_face('L')
        l = [x[::-1] for x in l][::-1]
        b = self.get_face('B')
        b = [x[::-1] for x in b][::-1]
        r = self.get_face('R')
        self.contents['L'] = f
        self.contents['B'] = l
        self.contents['R'] = b
        self.contents['F'] = r

    def rotate_cube_Z(self):
        '''
        Rotate the cube in the positive Z direction.
        '''
        self.rotate_cube_X()
        self.rotate_cube_Y()
        for i in range(3):
            self.rotate_cube_X()


    def display(self):
        '''
        Return a string version of the cube representation.
        '''

        return u.display(self.contents, self.size)

    def test_faces(self):
        '''
        Load the representation with unique characters.  For testing.
        '''

        self.contents = u.test_faces(self.size)

if __name__ == '__main__':
    rep = RubiksRep(3)
    rep.test_faces()
    print(rep.display())
    rep.rotate_cube_Z()
    print(rep.display())
