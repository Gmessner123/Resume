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
    
    def pickHighest(self, d):
        '''Returns a (move, count) tuple  corresponding to the highest win count
        in the dictionary d of the form {move, winCount}.'''
        maxWins = 0
        for count in d.values():
            if count > maxWins:
                maxWins = count
        for move in d.keys():
            if d[move] == maxWins:
                return (move, maxWins)        

    def pickLowest(self, d):
        '''Returns a (move, count) tuple corresponding to the lowest win count  
        in the dictionary d of the form {move, winCount}.'''
        minWins = self.n
        for count in d.values():
            if count < minWins:
                minWins = count
        for move in d.keys():
            if d[move] == minWins:
                return (move, minWins)
            
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
        oppWinCounts = {}
        cloneBoard = board.clone()
        for j in moves: # my move
            cloneBoard.makeMove(j, player) 
            newMoves = cloneBoard.possibleMoves()
            oppWinCounts2 = {}
            for k in newMoves: # opp move
                cloneBoard.makeMove(k, 3 - player)
                newMoves1 = cloneBoard.possibleMoves()
                oppWinCounts3 = {}
                for l in newMoves1: # my move
                    cloneBoard.makeMove(l, player)
                    newMoves2 = cloneBoard.possibleMoves()
                    oppWinCounts4 = {}
                    for m in newMoves2: # opp move
                        cloneBoard.makeMove(m, 3 - player)
                        numWins = 0
                        cloneBoard2 = cloneBoard.clone()
                        for s in range(0, self.n):
                            sim = Connect4Simulator(cloneBoard2, self.player, \
                                                self.player, player)
                            result = sim.simulate()
                            if result == 3 - player:
                                numWins += 1 
                            cloneBoard2 = cloneBoard.clone()
                        oppWinCounts4[m] = numWins
                        cloneBoard.unmakeMove(m)
                    (mov3, winNum3) = self.pickHighest(oppWinCounts4)
                    oppWinCounts3[l] = winNum3
                    cloneBoard.unmakeMove(l)
                (mov2, winNum2) = self.pickLowest(oppWinCounts3)
                oppWinCounts2[k] = winNum2
                cloneBoard.unmakeMove(k)
            (mov, winNum) = self.pickHighest(oppWinCounts2)
            oppWinCounts[j] = winNum
            cloneBoard.unmakeMove(j)
        (finalMove, wins) = self.pickLowest(oppWinCounts)
        return finalMove

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