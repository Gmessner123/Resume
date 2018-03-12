import random
from Connect4Simulator import *
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
            winCounts[j] = numWins
        return winCounts

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
        winCounts = self.getWinProbs(board, player, moves)
        maxWins = 0
        for val in winCounts.values():
            if val > maxWins:
                maxWins = val
        for key in winCounts.keys():
            if winCounts[key] == maxWins:
                return key

def yolo():
    num = 0
    for i in range(0,7):
        for j in range(0,7):
            for k in range(0,7):
                for l in range(0,7):
                    num += 1
    print num
yolo()
                
