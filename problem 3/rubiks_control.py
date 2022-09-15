# Name: Kyle McGraw
# Login: kmcgraw
'''
Rubik's cube controller (interactive interface).
'''

import copy, random
import rubiks_cube as c
import rubiks_utils as u
from tkinter import *
import time

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
        if len(d) > 0:
            d.sort()
            d.reverse()
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


    def play(self, check_solved=True):
        '''Interactively solve Rubik's cube.'''

        root = Tk()
        root.geometry('800x600')
        canvas = Canvas(root, width=800, height=600)
        canvas.pack()
        cubes = []
        draw = [self.cube.get_state()[0].get_face('U'),
        self.cube.get_state()[0].get_face('F'),
        self.cube.get_state()[0].get_face('R')]
        colors = {'w' : '#ffffff', 'r' : '#ff0000', 'b' : '#0000ff',
        'o' : '#ffa500', 'g' : '#00ff00', 'y' : '#ffff00'}
        size = len(draw[0])
        for i in range(size):
            for j in range(size):
                cubes.append(canvas.create_polygon([400 + 20 * j - 20 * i,
                100 + 10 * j + 10 * i, 420 + 20 * j - 20 * i,
                110 + 10 * j + 10 * i, 400 + 20 * j - 20 * i,
                120 + 10 * j + 10 * i, 380 + 20 * j - 20 * i,
                110 + 10 * j + 10 * i], fill=colors[draw[0][i][j]],
                outline=colors[draw[0][i][j]]))
                cubes.append(canvas.create_polygon(
                [400 - 20 * size + 20 * j,
                100 + 10 * size + 10 * j + 20 * i,
                420 - 20 * size + 20 * j,
                110 + 10 * size + 10 * j + 20 * i,
                420 - 20 * size + 20 * j,
                130 + 10 * size + 10 * j + 20 * i,
                400 - 20 * size + 20 * j,
                120 + 10 * size + 10 * j + 20 * i],
                fill=colors[draw[1][i][j]], outline=colors[draw[1][i][j]]))
                cubes.append(canvas.create_polygon([400 + 20 * j,
                100 + 20 * size - 10 * j + 20 * i, 420 + 20 * j,
                90 + 20 * size - 10 * j + 20 * i, 420 + 20 * j,
                110 + 20 * size - 10 * j + 20 * i, 400 + 20 * j,
                120 + 20 * size - 10 * j + 20 * i],
                fill=colors[draw[2][i][j]], outline=colors[draw[2][i][j]]))

        entry = StringVar()
        cmd = ""
        moves = []
        entrybox = Entry(root, textvariable=entry)
        canvas.create_window(400, 500, window=entrybox)
        movetext = Text(root)
        canvas.create_window(150, 300, height=600, width=300, window=movetext)
        movetext.insert(END, "Moves:\n")
        cmdtext = Text(root)
        canvas.create_window(650, 300, height=600, width=300, window=cmdtext)
        t = ("Commands:\nq: quit\n-: undo\nsave <file>: saves user commands to"
        " a file\nload <file>: loads user commands from a file\ncmds: prints "
        "user commands\n<cmds>: executes any number of commands seperated by "
        "spaces")
        cmdtext.insert(END, t)
        done = False
        def command(event):
            cmd = entry.get()
            entrybox.delete(0, 'end')
            cmds = cmd.split()
            if len(cmds) >= 1:
                try:
                    if cmds[0] in ['q', 'quit']:
                        done = True

                    # Undo a move.
                    if len(cmds) == 1 and cmds[0] in ['-', 'undo']:
                        self.do_undo()
                        moves.pop()
                        movetext.delete(1.0, END)
                        movetext.insert(END, "Moves:\n" + " ".join(moves))

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

                    else:
                        # Save the cube state before moving.
                        self.history.append(self.cube.get_state())
                        movetext.insert(END, cmd + "\n")
                        for subcmd in cmds:
                            self.do_command(subcmd)
                        moves.append(cmd)
                        movetext.delete(1.0, END)
                        movetext.insert(END, "Moves:\n" + " ".join(moves))
                        if check_solved and self.cube.is_solved():
                            print('SOLVED!')

                except BadCommand as b:
                    print(f'Invalid command line: {cmd}')
                    print(b)
                    movetext.delete(1.0, END)
                    movetext.insert(END, "Moves:\n" + "  ".join(moves))

        root.bind('<Return>', command)

        while not done:
            # moves
            draw = [self.cube.get_state()[0].get_face('U'),
            self.cube.get_state()[0].get_face('F'),
            self.cube.get_state()[0].get_face('R')]
            for cube in cubes:
                canvas.delete(cube)
            cubes = []
            for i in range(size):
                for j in range(size):
                    cubes.append(canvas.create_polygon([400 + 20 * j - 20 * i,
                    100 + 10 * j + 10 * i, 420 + 20 * j - 20 * i,
                    110 + 10 * j + 10 * i, 400 + 20 * j - 20 * i,
                    120 + 10 * j + 10 * i, 380 + 20 * j - 20 * i,
                    110 + 10 * j + 10 * i], fill=colors[draw[0][i][j]],
                    outline=colors[draw[0][i][j]]))
                    cubes.append(canvas.create_polygon(
                    [400 - 20 * size + 20 * j,
                    100 + 10 * size + 10 * j + 20 * i,
                    420 - 20 * size + 20 * j,
                    110 + 10 * size + 10 * j + 20 * i,
                    420 - 20 * size + 20 * j,
                    130 + 10 * size + 10 * j + 20 * i,
                    400 - 20 * size + 20 * j,
                    120 + 10 * size + 10 * j + 20 * i],
                    fill=colors[draw[1][i][j]], outline=colors[draw[1][i][j]]))
                    cubes.append(canvas.create_polygon([400 + 20 * j,
                    100 + 20 * size - 10 * j + 20 * i, 420 + 20 * j,
                    90 + 20 * size - 10 * j + 20 * i, 420 + 20 * j,
                    110 + 20 * size - 10 * j + 20 * i, 400 + 20 * j,
                    120 + 20 * size - 10 * j + 20 * i],
                    fill=colors[draw[2][i][j]], outline=colors[draw[2][i][j]]))
            root.update()

if __name__ == '__main__':
    # Leave 'scramble' as True normally.
    # Make it False if you want to test rotations on a solved cube.
    scramble = True
    check_solved = scramble
    cube = RubiksControl(3, scramble)
    cube.play(check_solved)
