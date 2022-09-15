'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuLoadError(SudokuError):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append([])
            for j in range(9):
                self.board[i].append(0)
        self.moves = []

    def load(self, filename):
        '''Loads a sudoku from the file into the board.'''
        with open(filename, 'r') as f:
            i = 0
            for line in f:
                if len(line)-1 != 9:
                    raise SudokuLoadError("wrong number of characters in line, expected 9")
                for j in range(9):
                    if line[j] not in list(map(str, range(0, 10))):
                        raise SudokuLoadError("values must be integers between 0 and 9")
                    self.board[i][j] = int(line[j])
                i += 1
            if i != 9:
                raise SudokuLoadError("wrong number of lines in file, expected 9")
        self.moves = []

    def save(self, filename):
        '''Saves the sudoku to a file of the filename.'''
        with open(filename, 'w') as f:
            for row in self.board:
                for item in row:
                    f.write(str(item))
                f.write('\n')

    def show(self):
        '''Pretty-print the current board representation.'''
        print()
        print('   1 2 3 4 5 6 7 8 9 ')
        for i in range(9):
            if i % 3 == 0:
                print('  +-----+-----+-----+')
            print(f'{i + 1} |', end='')
            for j in range(9):
                if self.board[i][j] == 0:
                    print(end=' ')
                else:
                    print(f'{self.board[i][j]}', end='')
                if j % 3 != 2 :
                    print(end=' ')
                else:
                    print('|', end='')
            print()
        print('  +-----+-----+-----+')
        print()

    def move(self, row, col, val):
        '''Put the values into the cell of the given .'''
        if val not in range(1, 10):
            raise SudokuMoveError("invalid move, value must be between 1 and 9")
        if row < 1 or col < 1 or row > 9 or col > 9:
            raise SudokuMoveError("invalid move, coordinates must be between 0 and 9")
        if self.board[row - 1][col - 1] != 0:
            raise SudokuMoveError("invalid move, cell is not empty")
        if val in self.board[row - 1]:
            raise SudokuMoveError("invalid move, number already in row")
        for i in range(9):
            if self.board[i][col - 1] == val:
                raise SudokuMoveError("invalid move, number already in column")
        for i in range(3 * ((row - 1) // 3), 3 + 3 * ((row - 1) // 3)):
            for j in range(3 * ((col - 1) // 3), 3 + 3 * ((col - 1) // 3)):
                if self.board[i][j] == val:
                    raise SudokuMoveError("invalid move, number already in box")
        self.board[row - 1][col - 1] = val
        self.moves.append((row, col, val))

    def undo(self):
        '''Undoes last move.'''
        row, col, val = self.moves.pop()
        self.board[row - 1][col - 1] = 0

    def solve(self):
        done = False
        while(not done):
            x = input('Enter command:')
            try:
                if x == 'q':
                    done = True
                elif x == 'u':
                    self.undo()
                    self.show()
                elif len(x) > 1 and x[0:2] == 's ':
                    self.save(x[2:])
                elif len(x) == 3:
                    try:
                        self.move(int(x[0]), int(x[1]), int(x[2]))
                        self.show()
                    except ValueError:
                        raise SudokuCommandError("invalid command")
                else:
                    raise SudokuCommandError("invalid command")
            except SudokuCommandError as e:
                print(e, file=sys.stderr)
                print("Please try again")
            except SudokuMoveError as e:
                print(e, file=sys.stderr)
                print("Please try again")

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except FileNotFoundError as e:
            print(e)
        except SudokuLoadError as e:
            print(e)

    s.show()
    s.solve()
