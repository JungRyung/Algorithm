'''
TITLE   : 큐
URL     : https://www.acmicpc.net/problem/10845
DATE    : 21.08.30
'''
import sys
from collections import deque

q = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    input = list(sys.stdin.readline().split())
    command = input[0]
    if command == 'push':
        q.append(int(input[1]))
    elif command == 'pop':
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif command == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)