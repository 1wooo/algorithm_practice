import math
import sys
input = sys.stdin.readline

board = input()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    for i in range(len(board)):
        print(board[i], end="")
