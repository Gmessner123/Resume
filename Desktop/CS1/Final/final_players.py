# Name: Grant Messner
# CMS cluster login name: gmessner

'''
final_players.py

This module contains code for various bots that play Connect4 at varying 
degrees of sophistication.
'''

import random
from Connect4Simulator import *
import copy


class RandomPlayer:
    '''
    This player makes one of the possible moves on the game board,
    chosen at random.
    '''
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
        possibles = board.possibleMoves()
        assert possibles != []
        return random.choice(possibles)


class SimplePlayer:
    '''
    This player will always play a move that gives it a win if there is one.
    Otherwise, it picks a random legal move.
    '''

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
        return random.choice(moves)


class BetterPlayer:
    '''
    This player will always play a move that gives it a win if there is one.
    Otherwise, it tries all moves, collects all the moves which don't allow
    the other player to win immediately, and picks one of those at random.
    If there is no such move, it picks a random move.
    '''

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
        oppWinningMoves = []
        for j in moves:
            board.makeMove(j, player)
            newMoves = board.possibleMoves()
            for k in newMoves: 
                if board.isWinningMove(k, 3 - player):
                    oppWinningMoves.append(j)
            board.unmakeMove(j)
        goodMoves = copy.deepcopy(moves)
        for o in oppWinningMoves:
            if o in goodMoves:
                goodMoves.remove(o)
        if goodMoves != []:
            return random.choice(goodMoves)
        else:
            return random.choice(moves)

class Monty:
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
        maxWins = 0
        for val in winCounts.values():
            if val > maxWins:
                maxWins = val
        for key in winCounts.keys():
            if winCounts[key] == maxWins:
                return key
