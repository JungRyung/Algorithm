'''
TITLE   : AC
URL     : https://www.acmicpc.net/problem/5430
DATE    : 21.09.09
'''
import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    if n == 0:
        sys.stdin.readline()
        arr = []
    else:
        arr = list(sys.stdin.readline().strip()[1:-1].split(','))
    arr = deque(arr)
    reversed = False
    errored = False
    for command in p:
        if command == 'R':
            reversed = not reversed
        elif command == 'D':
            if len(arr) == 0:
                errored = True
                break
            else:
                if reversed:
                    arr.pop()
                else:
                    arr.popleft()
    if errored:
        print("error")
    else:
        if reversed:
            arr.reverse()
        print('[',','.join(arr),']',sep='')