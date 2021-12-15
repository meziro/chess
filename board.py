from config import *
import IO

class Board:
    def __init__(self, board=[], player=WHITE, turn=1, s=''):
        if len(board) == SIZE:
            self.board = board
        else:
            self.board = [
                         [-R, -N, -B, -K, -Q, -B, -N, -R],
                         [-P, -P, -P, -P, -P, -P, -P, -P],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0],
                         [P, P, P, P, P, P, P, P],
                         [R, N, B, K, Q, B, N, R]
                        ]
            self.turn = turn
            self.player = player
            self.s = s

    def print(self, turnmode=True, reverse=False):
        start = [SIZE - 1, 0]
        stop =[-1, SIZE]
        step = [-1, +1]
        print('\t  a   b   c   d   e   f   g   h')
        print('\t  - - - - - - - - - - - - - - -')
        for hori in range(SIZE):
            print('\t{}'.format(hori+1),end='')
            for vert in range(SIZE):
                print(' {} |'.format(IO.RetType(self.board[hori][vert])),end='')
            print('\t')           
            print('\t  - - - - - - - - - - - - - - -')
board=[a]
a = Board(board,True,True)
a.print()
