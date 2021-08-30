'''
TITLE   : 스택
URL     : https://www.acmicpc.net/problem/10828
DATE    : 21.08.30
'''
import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    input = list(sys.stdin.readline().split())
    command = input[0]
    if command == 'push':
        s.append(int(input[1]))
    elif command == 'pop':
        if len(s) > 0:
            print(s.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(s))
    elif command == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(s) > 0:
            print(s[-1])
        else:
            print(-1)