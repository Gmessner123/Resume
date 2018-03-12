'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass


class Sudoku:
    '''Interactively play the game of Sudoku.'''
    
    global boardList
    global moveList
    def __init__(self):
        '''Initializes the game. Stores the global variables boardList and 
        moveList to the class (representing the Sudoku board and the moves made
        in the game so far.'''
        self.boardList = []
        self.moveList = []
        
    def load(self, filename):
        '''Loads the Sudoku board from the file filename. Checks to make sure 
        that (1) the file exists, (2) the length of each line is exactly 9 
        characters, (3) each line only contains integers in the inclusive range
        0-9, and (4) there are only 9 lines in the file. If any of these 
        conditions are not met, an error is thrown. If all conditions are met,
        the boardList is filled with the data from the file filename.'''
        global boardList
        global moveList
        moveList = []
        boardList = []
        count = 0
        f = open(filename, 'r')
        if f == None:
            raise IOError('File does not exist.')
        while True:
            line = f.readline()
            if line == '':
                break
            if len(line) != 10:
                raise IOError('Length of each line must be 9 characters.')
            else:
                lst = []
                for c in line:
                    if c != '' and c !='\n':
                        if c not in ['0','1','2','3','4','5','6','7','8','9']:
                            raise IOError('Each line must only contain integers')
                        elif int(c) not in range(0, 10):
                            raise IOError('Integers must be in the range of 0-9.')
                        else:
                            lst.append(int(c))
                global boardList
                self.boardList.append(lst)
                count += 1
        f.close()
        if count != 9:
            raise IOError('There must be exactly 9 lines in the file.')
        
    def save(self, filename):
        '''Writes the current sudoku boardList to the file filename.'''
        n = open(filename, 'w')
        for i in range(0, 9):
            lst = self.boardList[i]
            s = ''
            for j in range(0, 9):
                s += str(lst[j])
            n.write(s)
        n.close()
    
    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.boardList[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.boardList[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print 
        
    def move(self, row, col, val):
        '''Attempts to place a the number val down on the game board at the row
        row and column col. If the number val already exists in the row, column,
        or box that it is trying to be placed into, an exception is thrown (and
        caught later in the "solve" method). If the value is valid, then it is
        added on to the boardList, and the tuple (row, col, val) is added on to
        the moveList.'''
        global boardList
        global moveList        
        if row not in range(1, 10) or col not in range(1, 10) or val not in \
           range(1,10):
            raise SudokuMoveError('Rows and columns must be in the range 1-9.')
        elif val in self.boardList[row - 1]:
            raise SudokuMoveError('Invalid move: Row conflict')
        for i in range(0,9):
            if self.boardList[i][col - 1] == val: 
                raise SudokuMoveError('Invalid move: Column conflict') 
            x = (row - 1) / 3 
            y = (col - 1) / 3
            for j in range(x * 3, x * 3 + 3):
                for k in range(y * 3, y * 3 + 3):
                    if self.boardList[j][k] == val: 
                        raise SudokuMoveError('Invalid move: Box conflict')
        self.boardList[row - 1][col - 1] = val
        move = (row, col, val)
        self.moveList.append(move)
    
    def undo(self):
        '''As long as the moveList is not empty (i.e., as long as at least 1 
        move has already been made), deletes the last element of the moveList 
        and replaces the space occupied by the move on the boardList with a 0
        (representing an empty space).'''
        global boardList
        global moveList
        if self.moveList != []:
            move = self.moveList.pop()
            (row, col, val) = move
            print 'Undoing last move...'
            self.boardList[row - 1][col - 1] = 0
    
    def solve(self):
        '''Executes an infinite loop in order to run the game. Accepts user 
        commands and proccesses them. The user has four (valid) commands:
        quit, undo, save, and move, represented by "q", "u", "s" (plus a file 
        name), and a string of three integers. If the command is not valid, it
        is caught here and an error message is displayed. Similarly, if a move
        attempt is invalid an error message is displayed here.'''
        while True:
            try:
                command = raw_input('Enter a command: ')
                if command == 'q':
                    break
                elif command == 'u':
                    self.undo()
                elif command[0:1] == 's':
                    c1 = command.strip()
                    self.save(c1[1:])
                elif len(command) == 3 and type(int(command)) is int:
                    row = int(command[0:1])
                    col = int(command[1:2])
                    val = int(command[2:3])
                    self.move(row, col, val)
                else:
                    raise SudokuCommandError('Invalid command.')
                self.show()
            except SudokuMoveError, e:
                print e
                self.show()
            except SudokuCommandError, e:
                print e
                self.show()
            except ValueError:
                print 'Invalid command.'
                self.show()
                
                
if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    s.solve()
