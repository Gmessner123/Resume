import random
from Connect4Simulator import *
from final_players import *
import copy
import final_board as f

class SuperPlayer:
    '''
    This player will randomly simulate games for each possible move,
    picking the one that has the highest probability of success.
    '''

    def __init__(self, n, player):
        '''
        Initialize the player using a simpler computer player.

        Arguments: 
          n      -- number of games to simulate.
          player -- the computer player
        '''
        assert n > 0
        self.player = player
        self.n = n
        
    def getWinProbs(self, board, player, moves):
        '''Calculates the win counts for the player player if they make a move
        in the list of valid moves moves given the current board state board and
        the number of simulations n.'''
        winCounts = {} 
        for j in moves:
            spot = self.getOpenSpot(board, j)
            cloneBoard = board.clone()
            cloneBoard.makeMove(j, player)
            numWins = 0
            for k in range(0, self.n):
                sim = Connect4Simulator(cloneBoard, self.player, self.player, \
                                        3 - player)
                result = sim.simulate()
                if result == player:
                    numWins += 1
                cloneBoard = board.clone()
                cloneBoard.makeMove(j, player)
            if (spot % 2 == 0 and self.getOddEven(board) == True) or \
               (spot % 2 == 1 and self.getOddEven(board) == False):
                winCounts[j] = numWins ** 2
            else:
                winCounts[j] = numWins
        return winCounts
    
    def getOddEven(self, board):
        '''Returns true if an even number of moves have been made on the board,
        false if an odd number have been made.'''
        total = 0
        for col in board.boardList:
            for i in col:
                if col[i] == 1 or col[i] == 2:
                    total += 1
        if total % 2 == 0:
            return True
        else:
            return False
         
    def pickHighest(self, d):
        '''Returns a (move, count) tuple  corresponding to the highest win count
        in the dictionary d of the form {move, winCount}.'''
        vals = d.values()
        maxWins = vals[0]
        for count in d.values():
            if count > maxWins:
                maxWins = count
        for move in d.keys():
            if d[move] == maxWins:
                return (move, maxWins)        

    def pickLowest(self, d):
        '''Returns a (move, count) tuple corresponding to the lowest win count  
        in the dictionary d of the form {move, winCount}.'''
        vals = d.values()
        minWins = vals[0]
        for count in d.values():
            if count < minWins:
                minWins = count
        for move in d.keys():
            if d[move] == minWins:
                return (move, minWins)
            
    def colThreats(self, board, player):
        ''''''
        rowMax = board.getRows()
        colMax = board.getCols()
        colThreats = []
        k = 0
        for i in board.boardList:
            num1s = 0
            for j in range(rowMax - 1, -1, -1):
                if i[j] == player:
                    num1s += 1
                    if num1s == 3 and j != 0 and i[j - 1] != (3 - player):
                        colThreats.append(k)
                elif i[j] == 3 - player:
                    num1s = 0
            k += 1
        if len(colThreats) > 1:
            return colThreats 
        else:
            return []
    
    def rowThreats(self, board, player): 
        ''''''
        rowMax = board.getRows()
        colMax = board.getCols()
        rowThreats = []
        k = 0
        for i in range(rowMax - 1, -1, -1):
            num1s = 0
            for j in range(0, colMax):
                if board.boardList[j][i] == player:
                    num1s += 1
                    if num1s == 3 and ((j != colMax - 1 and \
                        board.boardList[j + 1][i] != (3 - player)) or \
                                        (j > 2 and board.boardList[j - 3][i]\
                                        != (3 - player))):
                        rowThreats.append(k) 
                elif board.boardList[j][i] == 3 - player or \
                        board.boardList[j][i] == 0:
                    num1s = 0
            k += 1
        if len(rowThreats) > 1:
            return rowThreats  
        else:
            return []
        
    def posDiagThreats(self, board, player):
        ''''''
        rowMax = board.getRows()
        colMax = board.getCols()
        diagThreats = []    
        iStarts = [0, 0, 0, 1, 2, 3] #col
        jStarts = [3, 4, 5, 5, 5, 5] #row
        for k in range(0, 6):
            i = iStarts[k]
            j = jStarts[k]
            num1s = 0
            while (i < colMax and j >= 0):
                if board.boardList[i][j] == player:
                    num1s += 1
                    if num1s == 3 and ((j != 1 and i != (colMax - 1) \
                        and board.boardList[i + 1][j - 1] != (3 - player)) or \
                                        (j < (rowMax - 4) and i > 2 and board.boardList[i - 3][j + 3]\
                                        != (3 - player))):
                        diagThreats.append(k) 
                elif board.boardList[i][j] == 3 - player or \
                        board.boardList[i][j] == 0:
                    num1s = 0                
                i += 1
                j -= 1
        #if len(diagThreats) > 1:
        return diagThreats
        #else:
            #return []
            
                
    def negDiagThreats(self, board, player):
        ''''''
        rowMax = board.getRows()
        colMax = board.getCols()
        diagThreats = []    
        iStarts = [0, 0, 0, 1, 2, 3] #col
        jStarts = [2, 1, 0, 0, 0, 0] #row
        for k in range(0, 6):
            i = iStarts[k]
            j = jStarts[k]
            num1s = 0
            while (i < colMax and j < rowMax):
                if board.boardList[i][j] == player:
                    num1s += 1
                    if num1s == 3 and ((j != (rowMax - 1) and i != (colMax - 1) \
                        and board.boardList[i + 1][j + 1] != (3 - player)) or \
                                        (j > 2 and i > 2 and board.boardList[i - 3][j - 3]\
                                        != (3 - player))):
                        diagThreats.append(k) 
                elif board.boardList[i][j] == 3 - player or \
                        board.boardList[i][j] == 0:
                    num1s = 0                
                i += 1
                j += 1
        #if len(diagThreats) > 1:
        return diagThreats
        #else:
            #return []
            
    def getOpenSpot(self, board, col):
        '''Returns the lowest open spot in the column col on the board board.'''
        for i in range(len(board.boardList[col]) -1 , -1, -1):
            if board.boardList[col][i] == 0:
                return i        
            
    def chooseMove(self, board, player):
        '''
        Given the current board and player number, choose and return a move.

        Arguments:
          board  -- a Connect4Board instance
          player -- either 1 or 2

        Precondition: There must be at least one legal move.
        Invariant: The board state does not change.
        '''
        assert player in [1, 2]
        moves = board.possibleMoves()
        assert player != []        
        for i in moves:
            if board.isWinningMove(i, player):
                return i   
        cloneBoard = board.clone()
        threatBalances = {}
        winPossibilities = [[3, 4, 5, 5, 4, 3],[4, 6, 8, 8, 6, 4],\
                            [5, 8, 11, 11, 8, 5],[7, 10, 13, 13, 10, 7], \
                            [5, 8, 11, 11, 8, 5], [4, 6, 8, 8, 6, 4], \
                            [3, 4, 5, 5, 4, 3]]        
        for j in moves:
            cloneBoard.makeMove(j, player)
            '''
            threatBalance = len(self.rowThreats(cloneBoard, player)) + \
            len(self.colThreats(cloneBoard, player)) - \
            len(self.rowThreats(cloneBoard, 3 - player)) - \
            len(self.colThreats(cloneBoard, 3 - player))
            threatBalance += len(self.posDiagThreats(cloneBoard, player)) ** 2 - \
            len(self.posDiagThreats(cloneBoard, 3 - player)) ** 2 + \
            len(self.negDiagThreats(cloneBoard, player)) ** 2 - \
            len(self.negDiagThreats(cloneBoard, 3 - player)) ** 2
            '''
            threatBalance = len(self.rowThreats(cloneBoard, 3 - player)) + \
            len(self.colThreats(cloneBoard, 3 - player)) + \
            len(self.posDiagThreats(cloneBoard, 3 - player)) ** 2 + \
            len(self.negDiagThreats(cloneBoard, 3 - player)) ** 2           
            threatBalances[j] = threatBalance
            cloneBoard.unmakeMove(j)
        (move, maxBalance) = self.pickHighest(threatBalances)
        (move2, minBalance) = self.pickLowest(threatBalances)
        if maxBalance != minBalance:
            return move2  
        else:
            try:
                winCounts = self.getWinProbs(board, player, moves)
                (move3, maxWins) = self.pickHighest(winCounts)  
                return move3
            except TypeError:
                print threatBalances
                
                '''
                        else:
                            winSums = {}
                            for k in moves:
                                cloneBoard.makeMove(k, player)
                                newMoves = cloneBoard.possibleMoves()
                                sum1 = 0
                                for l in newMoves:
                                    spot = self.getOpenSpot(cloneBoard, l)
                                    sum1 += winPossibilities[l][spot]
                                winSums[k] = sum1
                                cloneBoard.unmakeMove(k)
                            (move3, maxSum) = self.pickHighest(winSums)
                            (move4, minSum) = self.pickLowest(winSums)
                            #if maxSum != minSum:
                            return move3
                            #else:
                            ''' 
            

'''
s = SimplePlayer()   
su = SuperPlayer(100, s)
b = f.Connect4Board()
b.makeMove(3, 1)
b.makeMove(3, 1)
b.makeMove(3, 1)
b.makeMove(3, 2)
b.makeMove(2, 1)
b.makeMove(4, 1)
b.makeMove(5, 2)

b.printBoard()
print su.colThreats(b, 1)
print su.rowThreats(b, 1)
'''





b = f.Connect4Board()  
s = SimplePlayer()
better = BetterPlayer()
m = Monty(10, s)
su = SuperPlayer(10, s) 
num1s = 0
num2s = 0
numTies = 0
for i in range(0, 10):
    sim = Connect4Simulator(b, su, m, random.choice((1,2)))
    r = sim.simulate()
    print r
    if r == 1:
        num1s += 1
    elif r == 2:
        num2s += 1
    elif r == 0:
        numTies +=1
    b = f.Connect4Board()
    
print (num1s, num2s, numTies)
