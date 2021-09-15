'''
TITLE   : 하얀 칸
URL     : https://www.acmicpc.net/problem/1100
DATE    : 21.09.15
'''
import sys

board = [list(sys.stdin.readline().strip()) for _ in range(8)]

is_white = True
sum = 0
for i in range(8):
    for j in range(8):
        if is_white:
            if board[i][j] == 'F':
                sum += 1
        is_white = not is_white
    is_white = not is_white
print(sum)