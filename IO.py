from config import *

def RetType(target):
    if type(target) is int:
        if target == EMPTY:
            return ' '
        elif target == P * BLACK:
            return '♙'
        elif target == R * BLACK:
            return '♖'
        elif target == N * BLACK:
            return '♘'
        elif target == B * BLACK:
            return '♗'
        elif target == Q * BLACK:
            return '♕'
        elif target == K * BLACK:
            return '♔'
        elif target == P * WHITE:
            return '♟'
        elif target == R * WHITE:
            return '♜'
        elif target == N * WHITE:
            return '♞'
        elif target == B * WHITE:
            return '♝'
        elif target == Q * WHITE:
            return '♛'
        elif target == K * WHITE:
            return '♚'
        else:
            return false

    elif type(target) is str:
        if target.isdecimal():
            return int(target)
        elif ord('a') <= ord(target) <= ord('h'):
            return ord(target) - ord('a') + 1
        elif target == 'P':
            return P
        elif target == 'R':
            return R
        elif target == 'N':
            return N
        elif target == 'B':
            return B
        elif target == 'Q':
            return Q
        elif target == 'K':
            return K
        else:
            return false
    else:
        return false

