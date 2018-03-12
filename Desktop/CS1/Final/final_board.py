# Name: Grant Messner
# CMS cluster login name: gmessner

'''
final_board.py

This module contains classes that implement the Connect-4 board object.
'''

import copy

class MoveError(Exception):
    '''
    Instances of this class are exceptions which are raised when
    an invalid move is made.
    '''
    pass

class BoardError(Exception):
    '''
    Instances of this class are exceptions which are raised when
    some erroneous condition relating to a Connect-Four board occurs.
    '''
    pass

class Connect4Board:
    '''
    Instance of this class manage a Connect-Four board, but do not
    manage the play of the game itself.
    '''
    
    global boardList
    
    def __init__(self):
        '''
        Initialize the board.
        '''
        global boardList
        boardList = []
        for i in range(0,7): # Filled as col, row
            lst = []
            for j in range(0,6):
                lst.append(0)
            boardList.append(lst)
        self.boardList = boardList

    def getRows(self):
        '''
        Return the number of rows.
        '''
        return len(self.boardList[0])

    def getCols(self):
        '''
        Return the number of columns.
        '''
        return len(self.boardList)

    def get(self, row, col):
        '''
        Arguments:
          row -- a valid row index
          col -- a valid column index

        Return value: the board value at (row, col).

        Raise a BoardError exception if the 'row' or 'col' value is invalid.
        '''
        rowMax = self.getRows() 
        colMax = self.getCols() 
        if row not in range(0, rowMax):
            raise BoardError('Row must be in the range of 0-%d'%(rowMax - 1))
        if col not in range(0, colMax):
            raise BoardError('Column must be in the range of 0-%d'%(colMax - 1))
        return self.boardList[col][rowMax - 1 - row]
    

    def clone(self):
        '''
        Return a clone of this board i.e. a new instance of this class
        such that changing the fields of the new instance will not
        affect the old instance.

        Return value: the new Connect4Board instance.
        '''
        bList = copy.deepcopy(self.boardList)
        c1 = Connect4Board()
        c1.boardList = bList
        return c1

    def possibleMoves(self):
        '''
        Compute the list of possible moves (i.e. a list of column numbers 
        corresponding to the columns which are not completely filled up).

        Return value: the list of possible moves
        '''
        moves = []
        for i in range(0, len(self.boardList)):
            if 0 in self.boardList[i]:
                moves.append(i)
        return moves

    def makeMove(self, col, player):
        '''
        Make a move on the specified column for the specified player.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: none

        Raise a MoveError exception if a move cannot be made because the column
        is filled up, or if the column index or player number is invalid.
        '''
        global boardList
        moves = self.possibleMoves()
        colMax = self.getCols()
        if col not in range(0, colMax):
            raise MoveError('Column must be in the range of 0-%d'%(colMax - 1)) 
        elif player not in (1,2):
            raise MoveError('Player number must be either 1 or 2')
        elif col not in moves:
            raise MoveError('Column is full')
        for i in range(len(self.boardList[col]) -1 , -1, -1):
            if self.boardList[col][i] == 0:
                self.boardList[col][i] = player
                break

    def unmakeMove(self, col):
        '''
        Unmake the last move made on the specified column.

        Arguments:
          col -- a valid column index

        Return value: none

        Raise a MoveError exception if there is no move to unmake, or if the
        column index is invalid.
        '''
        global boardList
        colMax = self.getCols()
        if col not in range(0, colMax):
            raise MoveError('Column must be in the range of 0-%d'%(colMax - 1)) 
        elif 1 not in self.boardList[col] and 2 not in \
             self.boardList[col]:
            raise MoveError('Column is empty')
        for i in range(0, len(self.boardList[col])):
            if self.boardList[col][i] != 0:
                self.boardList[col][i] = 0
                break     

    def isWin(self, col):
        '''
        Check to see if the last move played in column 'col' resulted in a win
        (four or more discs of the same color in a row in any direction).

        Argument: 
          col    -- a valid column index

        Return value: True if there is a win, else False

        Raise a BoardError exception if the column is empty (i.e. no move has
        ever been made in the column), or if the column index is invalid.
        '''
        moves = self.possibleMoves()
        colMax = self.getCols()
        if col not in range(0, colMax):
            raise BoardError('Column must be in the range of 0-%d'%(colMax - 1))
        elif col in moves and 1 not in self.boardList[col] and 2 not in \
             self.boardList[col]:
            raise BoardError('Column is empty') 
        lastRow = 0
        for i in range(0, len(self.boardList[col])):
            if self.boardList[col][i] != 0:
                lastRow = i
                break
        if self.checkRow(col, lastRow) != 0 or self.checkCol(col, lastRow) !=0 \
           or self.checkMinusDiag(col, lastRow) != 0 or \
           self.checkPlusDiag(col, lastRow) != 0:
            return True
        else:
            return False
                                                                           
        
    def checkRow(self, col, row):
        '''Checks to see if there is a win that occurrs across a row'''
        colMax = self.getCols()
        for i in range(col - 3, col + 1):
            num1s = 0
            num2s = 0
            for j in range(i, i + 4):
                if j in range(0, colMax):
                    if self.boardList[j][row] == 1:
                        num1s += 1
                    elif self.boardList[j][row] == 2:
                        num2s += 1
            if num1s == 4:
                return 1
            elif num2s == 4:
                return 2
        return 0
    
    def checkCol(self, col, row):
        '''Checks to see if there is a win that occurrs down a column'''
        rowMax = self.getRows()
        for i in range(row - 3, row + 1):
            num1s = 0
            num2s = 0
            for j in range(i, i + 4):
                if j in range(0, rowMax):
                    if self.boardList[col][j] == 1:
                        num1s += 1
                    elif self.boardList[col][j] == 2:
                        num2s += 1
            if num1s == 4:
                return 1
            elif num2s == 4:
                return 2
        return 0 
    
    def checkMinusDiag(self, col, row):
        '''Checks to see if there is a win that occurrs across a negative 
        diagonal (i.e., one that goes from northwest to southeast).'''
        rowMax = self.getRows()
        colMax = self.getCols()
        for k in range(-3, 1):
            num1s = 0
            num2s = 0
            i = row + k
            for j in range(col + k, col + k + 4):
                if j in range(0, colMax) and i in range(0, rowMax):
                    if self.boardList[j][i] == 1:
                        num1s += 1
                    elif self.boardList[j][i] == 2:
                        num2s += 1
                i += 1
            if num1s == 4:
                return 1
            elif num2s == 4:
                return 2
        return 0
    
    def checkPlusDiag(self, col, row):
        '''Checks to see if there is a win that occurrs across a negative 
        diagonal (i.e., one that goes from northwest to southeast).'''
        rowMax = self.getRows()
        colMax = self.getCols()
        for k in range(-3, 1):
            num1s = 0
            num2s = 0
            i = row - k
            for j in range(col + k, col + k + 4):
                if j in range(0, colMax) and i in range(0, rowMax):
                    if self.boardList[j][i] == 1:
                        num1s += 1
                    elif self.boardList[j][i] == 2:
                        num2s += 1
                i -= 1
            if num1s == 4:
                return 1
            elif num2s == 4:
                return 2
        return 0    

    def isDraw(self):
        '''
        Check to see if the board is a draw because there are no more
        columns to play in.

        Precondition: This assumes that there is no win on the board.

        Return value: True if there is a draw, else False
        '''
        for i in range(0, len(self.boardList)):
            if 0 in self.boardList[i]:
                return False
        return True

    def isWinningMove(self, col, player):
        '''
        Check to see if making the move 'col' by the player 'player'
        would result in a win.  The board state does not change.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: True if the move would result in a win, else False.

        Precondition: This assumes that the move can be made.
        '''
        self.makeMove(col, player)
        if self.isWin(col) == True:
            self.unmakeMove(col)
            return True
        else:
            self.unmakeMove(col)
            return False

    def isDrawingMove(self, col, player):
        '''
        Check to see if making the move 'col' by the player 'player'
        would result in a draw.  The board state does not change.

        Arguments:
          col    -- a valid column index
          player -- either 1 or 2

        Return value: True if the move would result in a draw, else False.

        Precondition: This assumes that the move can be made, and that the
        move has been checked to see that it does not result in a win.
        '''
        try:
            self.makeMove(col, player)
            if self.isDraw() == True:
                self.unmakeMove(col)
                return True
            else:
                self.unmakeMove(col)
                return False 
        except MoveError:
            return True
