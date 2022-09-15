# Name: Kyle McGraw
# Login: kmcgraw
'''
Rubik's cube controller (interactive interface).
'''

import copy, random
import rubiks_cube as c
import rubiks_utils as u

class BadCommand(Exception):
    '''
    This exception is raised when an invalid command is received.
    '''
    pass

class RubiksControl:
    '''
    This class implements an interactive Rubik's cube puzzle.
    '''

    def __init__(self, size, scramble=True):
        '''
        Initialize the cube representation.
        Initialize the set of basic commands.

        Arguments:
          size     -- the size of the cube (must be 2 or 3)
                   -- 2 means a 2x2x2 cube; 3 means a 3x3x3 cube
          scramble -- True if you want the cube scrambled
        '''
        assert size in [2, 3]
        self.cube = c.RubiksCube(size)
        self.history = []
        if scramble:
            self.cube.scramble()

        # Built-in commands.
        # Use lower-case for ease of typing.
        # Use double quotes since some commands use the single quote character.
        self.face_moves = \
          ["u", "u'", "d", "d'", "f", "f'",
           "b", "b'", "l", "l'", "r", "r'"]
        self.rotations = ["x", "x'", "y", "y'", "z", "z'"]
        self.user_commands = copy.deepcopy(u.user_commands)

    def do_save_commands(self, filename):
        '''Save user commands to a file.'''
        with open(filename, 'w') as outfile:
            for (cmd, contents) in self.user_commands.items():
                print(f'{cmd} {contents}', file=outfile)

    def do_load_commands(self, filename):
        '''Load user commands from a file.'''
        self.user_commands = {}
        with open(filename) as infile:
            for line in infile:
                words = line.split()
                assert len(words) >= 2
                cmd = words[0]
                contents = ' '.join(words[1:])
                self.user_commands[cmd] = contents

    def do_print_commands(self):
        '''Print user commands to the terminal.'''
        for (cmd, contents) in self.user_commands.items():
            print(f'{cmd} : {contents}')

    def do_add_command(self, name, cmds):
        '''
        Add a user command.

        Arguments:
          name -- the name of the command
          cmds -- a list of the commands that the name should expand to

        Return value: none
        '''
        assert type(name) is str
        assert type(cmds) is list
        self.user_commands[name] = ' '.join(cmds)

    def do_command(self, cmd):
        '''
        Execute a command.

        Arguments:
          cmd -- a command

        Return value: none
        '''
        assert type(cmd) is str
        cmds = cmd.split(' ')
        d = []
        for i in range(len(cmds)):
            if cmds[i] == '':
                d.append(i)
        for i in d:
            del cmds[i]
        dir = '+'
        for command in cmds:
            if command in self.face_moves:
                if len(command) > 1:
                    dir = '-'
                self.cube.move_face(command[0].upper(), dir)
                dir = '+'
            elif command in self.rotations:
                if len(command) > 1:
                    dir = '-'
                self.cube.rotate_cube(command[0].upper(), dir)
                dir = '+'
            elif command in self.user_commands:
                self.do_command(self.user_commands[command])
            else:
                raise BadCommand("Command does not exist")

    def do_undo(self):
        '''
        Undo the last move(s), restoring the previous state.
        '''
        if self.history == []:
            raise BadCommand('No moves to undo!')
        (rep, count) = self.history.pop()
        self.cube.put_state(rep, count)

    def solve(self):
        if self.cube.rep.size == 2:
            def topCorner(c1, c2, c3):
                found = False
                piece = [c1 + c2 + c3, c2 + c1 + c3, c1 + c3 + c2, c2 + c3 + c1,
                        c3 + c1 + c2, c3 + c2 + c1]
                for i in range(4):
                    if self.cube.get_state()[0].get_row('F', 1)[1] + \
                    self.cube.get_state()[0].get_row('D', 0)[1] + \
                    self.cube.get_state()[0].get_row('R', 1)[0] in piece:
                        found = True
                        break
                    self.do_command('d')
                    f.write("Move: d" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                if not found:
                    for i in range(4):
                        if self.cube.get_state()[0].get_row('U', 1)[1] + \
                        self.cube.get_state()[0].get_row('F', 0)[1] + \
                        self.cube.get_state()[0].get_row('R', 0)[0] in piece:
                            found = True
                            self.do_command("ufr->dfr")
                            f.write("Move: ufr->dfr" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            for j in range(i):
                                self.do_command("u'")
                                f.write("Move: u'" + "\n")
                                f.write(self.cube.display() + "\n")
                                f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        self.do_command('u')
                        f.write("Move: u" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                self.do_command("dfr->ufr")
                f.write("Move: dfr->ufr" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                if self.cube.get_state()[0].get_row('F', 0)[1] == c1:
                    self.do_command("ufr")
                    f.write("Move: ufr" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                elif self.cube.get_state()[0].get_row('R', 0)[0] == c1:
                    self.do_command("ufr'")
                    f.write("Move: ufr" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")

            def bottomFace(c1):
                while self.cube.get_state()[0].get_row('U', 0)[0] != c1 or\
                    self.cube.get_state()[0].get_row('U', 0)[1] != c1 or\
                    self.cube.get_state()[0].get_row('U', 1)[0] != c1 or\
                    self.cube.get_state()[0].get_row('U', 1)[1] != c1:
                    for i in range(4):
                        if self.cube.get_state()[0].get_row('U', 1)[0] == c1:
                            if self.cube.get_state()[0].get_row('U', 1)[1] == c1:
                                self.do_command('y2')
                                f.write("Move: y2" + "\n")
                                f.write(self.cube.display() + "\n")
                                f.write("Move count: " + str(self.cube.count) + "\n\n")
                                if self.cube.get_state()[0].get_row('F', 0)[0] != c1:
                                    self.do_command('y')
                                    f.write("Move: y" + "\n")
                                    f.write(self.cube.display() + "\n")
                                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                            self.do_command('ep')
                            f.write("Move: ep" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        self.do_command('y')
                        f.write("Move: y" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                        if i == 3:
                            self.do_command('ep')
                            f.write("Move: ep" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")

            def bottomCorners():
                for i in range(4):
                    if self.cube.is_solved():
                        return
                    self.do_command("u")
                    f.write("Move: u" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                i = 0
                while i < 4:
                    if self.cube.get_state()[0].get_row('F', 0)[0] ==\
                    self.cube.get_state()[0].get_row('F', 0)[1]:
                        self.do_command("y2 r' f r' b2 r f' r' b2 r2")
                        f.write("Move: y2 r' f r' b2 r f' r' b2 r2" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                        break
                    self.do_command("y")
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                    if i == 3:
                        self.do_command("y2 r' f r' b2 r f' r' b2 r2")
                        f.write("Move: y2 r' f r' b2 r f' r' b2 r2" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                        i = -1
                    i += 1
                while not self.cube.is_solved():
                    self.do_command("u")
                    f.write("Move: u" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")

            with open("2x2solve.txt", 'w') as f:
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                faces = ['U', 'D', 'F', 'B', 'L', 'R']
                colors = ['b', 'g', 'o', 'r', 'w', 'y']
                edgeColors = ['r', 'b', 'o', 'g']
                for i in range(len(edgeColors)):
                    topCorner('w', edgeColors[i], edgeColors[(i + 1) % \
                    len(edgeColors)])
                    self.do_command('y')
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                self.do_command('x2')
                f.write("Move: x2" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                bottomFace('y')
                bottomCorners()
                f.write('SOLVED in ' + str(self.cube.count) + " moves!")
            with open("2x2solve.txt", 'r') as f:
                print(f.read())
        if self.cube.rep.size == 3:

            def topEdge(c1, c2):
                found = False
                piece = [c1 + c2, c2 + c1]
                for i in range(4):
                    if self.cube.get_state()[0].get_row('F', 2)[1] + \
                    self.cube.get_state()[0].get_row('D', 0)[1] in piece:
                        found = True
                        break
                    self.do_command('d')
                    f.write("Move: d" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                if not found:
                    for i in range(4):
                        if self.cube.get_state()[0].get_row('F', 1)[0] + \
                        self.cube.get_state()[0].get_row('L', 1)[2] in piece:
                            found = True
                            self.do_command("f'")
                            f.write("Move: f'" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        if self.cube.get_state()[0].get_row('F', 1)[2] + \
                        self.cube.get_state()[0].get_row('R', 1)[0] in piece:
                            found = True
                            self.do_command("f")
                            f.write("Move: f" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        self.do_command('e')
                        f.write("Move: e" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                if not found:
                    for i in range(4):
                        if self.cube.get_state()[0].get_row('U', 2)[1] + \
                        self.cube.get_state()[0].get_row('F', 0)[1] in piece:
                            found = True
                            self.do_command("f2")
                            f.write("Move: f2" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            for j in range(i):
                                self.do_command("u'")
                                f.write("Move: u'" + "\n")
                                f.write(self.cube.display() + "\n")
                                f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        self.do_command('u')
                        f.write("Move: u" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                if self.cube.get_state()[0].get_row('F', 2)[1] == c1:
                    self.do_command("df->uf'")
                    f.write("Move: df->uf'" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                elif self.cube.get_state()[0].get_row('D', 0)[1] == c1:
                    self.do_command("f2")
                    f.write("Move: f2" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")

            def topCorner(c1, c2, c3):
                found = False
                piece = [c1 + c2 + c3, c2 + c1 + c3, c1 + c3 + c2, c2 + c3 + c1,
                        c3 + c1 + c2, c3 + c2 + c1]
                for i in range(4):
                    if self.cube.get_state()[0].get_row('F', 2)[2] + \
                    self.cube.get_state()[0].get_row('D', 0)[2] + \
                    self.cube.get_state()[0].get_row('R', 2)[0] in piece:
                        found = True
                        break
                    self.do_command('d')
                    f.write("Move: d" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                if not found:
                    for i in range(4):
                        if self.cube.get_state()[0].get_row('U', 2)[2] + \
                        self.cube.get_state()[0].get_row('F', 0)[2] + \
                        self.cube.get_state()[0].get_row('R', 0)[0] in piece:
                            found = True
                            self.do_command("ufr->dfr")
                            f.write("Move: ufr->dfr" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            for j in range(i):
                                self.do_command("u'")
                                f.write("Move: u'" + "\n")
                                f.write(self.cube.display() + "\n")
                                f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        self.do_command('u')
                        f.write("Move: u" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                self.do_command("dfr->ufr")
                f.write("Move: dfr->ufr" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                if self.cube.get_state()[0].get_row('F', 0)[2] == c1:
                    self.do_command("ufr")
                    f.write("Move: ufr" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                elif self.cube.get_state()[0].get_row('R', 0)[0] == c1:
                    self.do_command("ufr'")
                    f.write("Move: ufr" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")

            def middleEdge(c1, c2):
                found = False
                piece = [c1 + c2, c2 + c1]
                for i in range(4):
                    if self.cube.get_state()[0].get_row('F', 2)[1] + \
                    self.cube.get_state()[0].get_row('D', 0)[1] in piece:
                        found = True
                        break
                    self.do_command('d')
                    f.write("Move: d" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                if not found:
                    for i in range(4):
                        if self.cube.get_state()[0].get_row('F', 1)[2] + \
                        self.cube.get_state()[0].get_row('R', 1)[0] in piece:
                            found = True
                            self.do_command("r' d r d f d' f' d2")
                            f.write("Move: r' d r d f d' f' d2" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                            for j in range(i):
                                self.do_command("e'")
                                f.write("Move: e'" + "\n")
                                f.write(self.cube.display() + "\n")
                                f.write("Move count: " + str(self.cube.count) + "\n\n")
                            break
                        self.do_command('e')
                        f.write("Move: e" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                if not found:
                    print(c1, c2, "doesn't exist", self.cube.display())
                    quit()
                if self.cube.get_state()[0].get_row('F', 2)[1] == c1:
                    self.do_command("d' r' d r d f d' f'")
                    f.write("Move: d' r' d r d f d' f'" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                elif self.cube.get_state()[0].get_row('D', 0)[1] == c1:
                    self.do_command("r' d r d f d' f' r' d r d f d' f'")
                    f.write("Move: r' d r d f d' f' r' d r d f d' f'" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")

            def bottomCross():
                i = 0
                while i < 4:
                    i += 1
                    if self.cube.get_state()[0].get_row('U', 2)[1] != \
                    self.cube.get_state()[0].get_row('U', 1)[1]:
                        i = 0
                        self.do_command('fru')
                        f.write("Move: fru" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                    self.do_command('u')
                    f.write("Move: u" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                while self.cube.get_state()[0].get_row('F', 0)[1] != \
                self.cube.get_state()[0].get_row('F', 1)[1]:
                    self.do_command('u')
                    f.write("Move: u" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                self.do_command('y2')
                f.write("Move: y2" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                if self.cube.get_state()[0].get_row('L', 0)[1] != \
                self.cube.get_state()[0].get_row('L', 1)[1]:
                    if self.cube.get_state()[0].get_row('F', 0)[1] != \
                    self.cube.get_state()[0].get_row('L', 1)[1]:
                        self.do_command("u ep u'")
                        f.write("Move: u ep u" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                    self.do_command('ep')
                    f.write("Move: ep" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                self.do_command('y')
                f.write("Move: y" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                # print(self.cube.display())
                if self.cube.get_state()[0].get_row('L', 0)[1] != \
                self.cube.get_state()[0].get_row('L', 1)[1]:
                    self.do_command('ep')
                    f.write("Move: ep" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")

            def bottomCorners(bot):
                corners = False
                while not corners:
                    for i in range(4):
                        c1 = self.cube.get_state()[0].get_row('U', 1)[1]
                        c2 = self.cube.get_state()[0].get_row('F', 1)[1]
                        c3 = self.cube.get_state()[0].get_row('L', 1)[1]
                        c4 = self.cube.get_state()[0].get_row('R', 1)[1]
                        piece1 = [c1 + c2 + c3, c2 + c1 + c3, c1 + c3 + c2, c2 + c3 + c1,
                                c3 + c1 + c2, c3 + c2 + c1]
                        piece2 = [c1 + c2 + c4, c2 + c1 + c4, c1 + c4 + c2, c2 + c4 + c1,
                                c4 + c1 + c2, c4 + c2 + c1]
                        if self.cube.get_state()[0].get_row('U', 2)[0] + \
                        self.cube.get_state()[0].get_row('F', 0)[0] + \
                        self.cube.get_state()[0].get_row('L', 0)[2] in piece1:
                            while self.cube.get_state()[0].get_row('U', 2)[2] + \
                            self.cube.get_state()[0].get_row('F', 0)[2] + \
                            self.cube.get_state()[0].get_row('R', 0)[0] not in piece2:
                                self.do_command("r  u' l' u r' u' l u")
                                f.write("Move: r  u' l' u r' u' l u" + "\n")
                                f.write(self.cube.display() + "\n")
                                f.write("Move count: " + str(self.cube.count) + "\n\n")
                            corners = True
                            break
                        self.do_command('y')
                        f.write("Move: y" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                    if not corners:
                        self.do_command("r  u' l' u r' u' l u")
                        f.write("Move: r  u' l' u r' u' l u" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")
                while not self.cube.is_solved():
                    while self.cube.get_state()[0].get_row('U', 2)[2] != bot:
                            self.do_command("r' d' r d")
                            f.write("Move: r' d' r d" + "\n")
                            f.write(self.cube.display() + "\n")
                            f.write("Move count: " + str(self.cube.count) + "\n\n")
                    if not self.cube.is_solved():
                        self.do_command('u')
                        f.write("Move: u" + "\n")
                        f.write(self.cube.display() + "\n")
                        f.write("Move count: " + str(self.cube.count) + "\n\n")

            with open("3x3solve.txt", 'w') as f:
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                faces = ['U', 'D', 'F', 'B', 'L', 'R']
                colors = ['b', 'g', 'o', 'r', 'w', 'y']
                while True:
                    self.do_command('x')
                    f.write("Move: x" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                    if self.cube.get_state()[0].get_row('F', 1)[1] == 'w':
                        break
                    self.do_command('y')
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                    if self.cube.get_state()[0].get_row('F', 1)[1] == 'w':
                        break
                self.do_command('x')
                f.write("Move: x" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                edgeColors = ['r', 'b', 'o', 'g']
                for color in edgeColors:
                    topEdge('w', color)
                    self.do_command('y')
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                for i in range(len(edgeColors)):
                    topCorner('w', edgeColors[i], edgeColors[(i + 1) % \
                    len(edgeColors)])
                    self.do_command('y')
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                while self.cube.get_state()[0].get_row('F', 0)[1] != \
                self.cube.get_state()[0].get_row('F', 1)[1]:
                    self.do_command('u')
                    f.write("Move: u" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                while self.cube.get_state()[0].get_row('F', 1)[1] != 'r':
                    self.do_command('y')
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                for i in range(len(edgeColors)):
                    middleEdge(edgeColors[i], edgeColors[(i + 1) % \
                    len(edgeColors)])
                    self.do_command('y')
                    f.write("Move: y" + "\n")
                    f.write(self.cube.display() + "\n")
                    f.write("Move count: " + str(self.cube.count) + "\n\n")
                self.do_command('x2')
                f.write("Move: x2" + "\n")
                f.write(self.cube.display() + "\n")
                f.write("Move count: " + str(self.cube.count) + "\n\n")
                bottomCross()
                bottomCorners('y')
                f.write('SOLVED in ' + str(self.cube.count) + " moves!")
            with open("3x3solve.txt", 'r') as f:
                print(f.read())

    def play(self, check_solved=True):
        '''Interactively solve Rubik's cube.'''

        while True:
            print(self.cube.display())
            print(f'Move count: {self.cube.count}\n')

            if check_solved and self.cube.is_solved():
                print('SOLVED!')
                break

            cmd = input('cube> ')
            cmds = cmd.split()
            if len(cmds) < 1:
                continue

            try:
                if cmds[0] in ['q', 'quit']:
                    break

                # Undo a move.
                if len(cmds) == 1 and cmds[0] in ['-', 'undo']:
                    self.do_undo()

                # Save the commands to a file.
                elif len(cmds) == 2 and cmds[0] == 'save':
                    self.do_save_commands(cmds[1])

                # Load commands from a file.
                elif len(cmds) == 2 and cmds[0] == 'load':
                    self.do_load_commands(cmds[1])

                # Print all commands.
                elif len(cmds) == 1 and cmds[0] == 'cmds':
                    self.do_print_commands()

                # Add a new command if the second word is ':'.
                elif len(cmds) > 2 and cmds[1] == ':':
                    self.do_add_command(cmds[0], cmds[2:])

                elif len(cmds) == 1 and cmds[0] == 'solve':
                    self.solve()

                else:
                    # Save the cube state before moving.
                    self.history.append(self.cube.get_state())

                    for subcmd in cmds:
                        self.do_command(subcmd)

            except BadCommand as b:
                print(f'Invalid command line: {cmd}')
                print(b)


if __name__ == '__main__':
    # Leave 'scramble' as True normally.
    # Make it False if you want to test rotations on a solved cube.
    scramble = True
    check_solved = scramble
    cube = RubiksControl(2, scramble)
    cube.solve()
