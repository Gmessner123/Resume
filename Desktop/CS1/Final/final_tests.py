'''
Tests of the 2016 CS 1 final exam, part A.
This is supplied to the students.
'''

import nose
from nose.tools import assert_raises
import random, copy

from final_board import *

class TestInvalid(Exception): pass
class TestError(Exception): pass

def get_contents(board):
    '''Return the contents of the entire board as a list of lists.'''

    contents = []
    for r in range(6):
        row = []
        for c in range(7):
            row.append(board.get(r, c))
        contents.append(row)
    return contents

def same_contents(board1, board2):
    '''Return True if two boards have the same contents.'''
    return get_contents(board1) == get_contents(board2)

def impossible_moves(moves):
    '''Return a list of all valid moves that are not in a list of moves.'''
    return list(set(range(7)) - set(moves))

# ---------------------------------------------------------------------- 
# The tests.
# ---------------------------------------------------------------------- 

def test_accessors():
    '''Test the constructor and accessors.'''

    for i in range(10):
        b = Connect4Board()

        # Check basic accessors.
        assert b.getRows() == 6
        assert b.getCols() == 7
        for row in range(6):
            for col in range(7):
                assert b.get(row, col) == 0

        # Check exception handling.
        assert_raises(BoardError, b.get, -1, 0)
        assert_raises(BoardError, b.get, 6, 0)
        assert_raises(BoardError, b.get, 0, -1)
        assert_raises(BoardError, b.get, 0, 7)

        b.makeMove(3, 1)
        b.makeMove(3, 2)
        b.makeMove(2, 1)
        b.makeMove(1, 2)
        assert b.get(0, 3) == 1
        assert b.get(1, 3) == 2
        assert b.get(0, 2) == 1
        assert b.get(0, 1) == 2

def test_clone():
    '''Test that cloning the board gives two independent boards.'''

    b = Connect4Board()
    b.makeMove(3, 1)
    b.makeMove(3, 2)
    b.makeMove(2, 1)
    # Make sure boards are independent!
    b2 = b.clone()
    b2.makeMove(2, 2)
    assert b2.get(1, 2) == 2
    assert b.get(1, 2) == 0

def test_play_to_end():
    '''
    Test that playing alternating valid moves will result eventually
    in a win or a draw.  This tests several different methods.
    '''
    for i in range(10):
        b = Connect4Board()
        #b.printBoard()
        player = 1
        count = 0

        while True:
            moves = b.possibleMoves()

            if moves == []:
                assert False  # something went wrong

            for move in moves:
                # Check that all possible moves are valid.
                assert move in range(7), 'invalid possible move'

                try:
                    b2 = b.clone()
                    b.makeMove(move, player)
                    b.unmakeMove(move)
                    assert same_contents(b, b2)
                except MoveError:
                    assert False, 'invalid possible move'
                except:
                    assert False, 'invalid possible move and exception'

            # Check that all impossible moves are invalid.
            for move in impossible_moves(moves):
                assert_raises(MoveError, b.makeMove, move, player)

            # Check that out-of-bound moves raise MoveError exceptions.
            for move in [-1, 7, 9]:
                assert_raises(MoveError, b.makeMove, move, player)

            col = random.choice(moves)
            # Check that moving an invalid player raises a MoveError exception.
            assert_raises(MoveError, b.makeMove, move, 3)
            assert_raises(MoveError, b.makeMove, move, 0)

            b.makeMove(col, player)
            if b.isWin(col) or b.isDraw():
                break
            player = 3 - player
            count += 1

def test_makeMove():
    b = Connect4Board()
    # Test exception handling.
    assert_raises(MoveError, b.makeMove, -1, 1)
    assert_raises(MoveError, b.makeMove, 7, 1)
    assert_raises(MoveError, b.makeMove, 3, 0)
    assert_raises(MoveError, b.makeMove, 3, 3)
    # Test that making a move with the same player over and over
    # is _not_ an error (boards don't enforce alternating players).
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    # Test that making a move in a full column raises a MoveError exception.
    assert_raises(MoveError, b.makeMove, 3, 1)

def test_unmakeMove():
    b = Connect4Board()
    b2 = b.clone()
    b.makeMove(3, 1)
    # Test exception handling.
    # Invalid columns.
    assert_raises(MoveError, b.unmakeMove, -1)
    assert_raises(MoveError, b.unmakeMove, 7)
    b.unmakeMove(3)
    assert same_contents(b, b2)
    # Unmaking a move from an empty column.
    assert_raises(MoveError, b.unmakeMove, 3)

def test_isWin():
    # Test detection of horizontal wins.
    b = Connect4Board()
    b.makeMove(0, 1)
    assert not b.isWin(0)
    b.makeMove(1, 1)
    assert not b.isWin(1)
    b.makeMove(2, 1)
    assert not b.isWin(2)
    b.makeMove(3, 1)
    assert b.isWin(3)

    # Test detection of vertical wins.
    b = Connect4Board()
    b.makeMove(0, 1)
    assert not b.isWin(0)
    b.makeMove(0, 1)
    assert not b.isWin(0)
    b.makeMove(0, 1)
    assert not b.isWin(0)
    b.makeMove(0, 1)
    assert b.isWin(0)

    # Test detection of upward diagonal wins.
    b = Connect4Board()
    b.makeMove(0, 1)
    assert not b.isWin(0)
    b.makeMove(1, 2)
    assert not b.isWin(1)
    b.makeMove(1, 1)
    assert not b.isWin(1)
    b.makeMove(2, 2)
    assert not b.isWin(2)
    b.makeMove(2, 2)
    assert not b.isWin(2)
    b.makeMove(2, 1)
    assert not b.isWin(2)
    b.makeMove(3, 2)
    assert not b.isWin(3)
    b.makeMove(3, 2)
    assert not b.isWin(3)
    b.makeMove(3, 2)
    assert not b.isWin(3)
    b.makeMove(3, 1)
    assert b.isWin(3)

    # Test detection of downward diagonal wins.
    b = Connect4Board()
    b.makeMove(3, 1)
    assert not b.isWin(3)
    b.makeMove(2, 2)
    assert not b.isWin(2)
    b.makeMove(2, 1)
    assert not b.isWin(2)
    b.makeMove(1, 2)
    assert not b.isWin(1)
    b.makeMove(1, 2)
    assert not b.isWin(1)
    b.makeMove(1, 1)
    assert not b.isWin(1)
    b.makeMove(0, 2)
    assert not b.isWin(0)
    b.makeMove(0, 2)
    assert not b.isWin(0)
    b.makeMove(0, 2)
    assert not b.isWin(0)
    b.makeMove(0, 1)
    assert b.isWin(0)

    # Test exception handling.
    b = Connect4Board()
    b.makeMove(0, 1)
    b.makeMove(1, 1)
    b.makeMove(2, 1)
    assert_raises(BoardError, b.isWin, -1)
    assert_raises(BoardError, b.isWin, 7)
    assert_raises(BoardError, b.isWin, 3)  # empty column

def test_isDraw():
    b = Connect4Board()
    # Make the following drawn board:
    #
    #  1212122
    #  1212121
    #  2121212
    #  2121212
    #  1212121
    #  1212121

    b.makeMove(0, 1)
    b.makeMove(0, 1)
    b.makeMove(0, 2)
    b.makeMove(0, 2)
    b.makeMove(0, 1)
    b.makeMove(0, 1)

    b.makeMove(1, 2)
    b.makeMove(1, 2)
    b.makeMove(1, 1)
    b.makeMove(1, 1)
    b.makeMove(1, 2)
    b.makeMove(1, 2)

    b.makeMove(2, 1)
    b.makeMove(2, 1)
    b.makeMove(2, 2)
    b.makeMove(2, 2)
    b.makeMove(2, 1)
    b.makeMove(2, 1)

    b.makeMove(3, 2)
    b.makeMove(3, 2)
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    b.makeMove(3, 2)
    b.makeMove(3, 2)

    b.makeMove(4, 1)
    b.makeMove(4, 1)
    b.makeMove(4, 2)
    b.makeMove(4, 2)
    b.makeMove(4, 1)
    b.makeMove(4, 1)

    b.makeMove(5, 2)
    b.makeMove(5, 2)
    b.makeMove(5, 1)
    b.makeMove(5, 1)
    b.makeMove(5, 2)
    b.makeMove(5, 2)

    b.makeMove(6, 1)
    b.makeMove(6, 1)
    b.makeMove(6, 2)
    b.makeMove(6, 2)
    b.makeMove(6, 1)
    b.makeMove(6, 2)

    for i in range(7):
        assert not b.isWin(i)
    assert b.isDraw()

def test_isWinningMove():
    # Test detection of horizontal wins.
    b = Connect4Board()
    b.makeMove(0, 1)
    b.makeMove(1, 1)
    b.makeMove(2, 1)
    assert b.isWinningMove(3, 1)

    # Test detection of vertical wins.
    b = Connect4Board()
    b.makeMove(0, 1)
    b.makeMove(0, 1)
    b.makeMove(0, 1)
    assert b.isWinningMove(0, 1)

    # Test detection of upward diagonal wins.
    b = Connect4Board()
    b.makeMove(0, 1)
    b.makeMove(1, 2)
    b.makeMove(1, 1)
    b.makeMove(2, 2)
    b.makeMove(2, 2)
    b.makeMove(2, 1)
    b.makeMove(3, 2)
    b.makeMove(3, 2)
    b.makeMove(3, 2)
    assert b.isWinningMove(3, 1)

    # Test detection of downward diagonal wins.
    b = Connect4Board()
    b.makeMove(3, 1)
    b.makeMove(2, 2)
    b.makeMove(2, 1)
    b.makeMove(1, 2)
    b.makeMove(1, 2)
    b.makeMove(1, 1)
    b.makeMove(0, 2)
    b.makeMove(0, 2)
    b.makeMove(0, 2)
    assert b.isWinningMove(0, 1)

def test_isDrawingMove():
    b = Connect4Board()
    # Make the following drawn board:
    #
    #  1212122
    #  1212121
    #  2121212
    #  2121212
    #  1212121
    #  1212121

    b.makeMove(0, 1)
    b.makeMove(0, 1)
    b.makeMove(0, 2)
    b.makeMove(0, 2)
    b.makeMove(0, 1)
    b.makeMove(0, 1)

    b.makeMove(1, 2)
    b.makeMove(1, 2)
    b.makeMove(1, 1)
    b.makeMove(1, 1)
    b.makeMove(1, 2)
    b.makeMove(1, 2)

    b.makeMove(2, 1)
    b.makeMove(2, 1)
    b.makeMove(2, 2)
    b.makeMove(2, 2)
    b.makeMove(2, 1)
    b.makeMove(2, 1)

    b.makeMove(3, 2)
    b.makeMove(3, 2)
    b.makeMove(3, 1)
    b.makeMove(3, 1)
    b.makeMove(3, 2)
    b.makeMove(3, 2)

    b.makeMove(4, 1)
    b.makeMove(4, 1)
    b.makeMove(4, 2)
    b.makeMove(4, 2)
    b.makeMove(4, 1)
    b.makeMove(4, 1)

    b.makeMove(5, 2)
    b.makeMove(5, 2)
    b.makeMove(5, 1)
    b.makeMove(5, 1)
    b.makeMove(5, 2)
    b.makeMove(5, 2)

    b.makeMove(6, 1)
    b.makeMove(6, 1)
    b.makeMove(6, 2)
    b.makeMove(6, 2)
    b.makeMove(6, 1)
    assert b.isDrawingMove(6, 2)

if __name__ == '__main__':
    nose.runmodule()


