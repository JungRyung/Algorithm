'''
TITLE   : 덱
URL     : https://www.acmicpc.net/problem/10866
DATE    : 21.08.31
'''
import sys

deque = []
n = int(sys.stdin.readline())
for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_back":
        deque.append(int(command[1]))
    elif command[0] == "push_front":
        deque.insert(0,int(command[1]))
    elif command[0] == "front":
        if len(deque) > 0:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(deque) > 0:
            print(deque[-1])
        else:
            print(-1)
    elif command[0] == "size":
        print(len(deque))
    elif command[0] == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "pop_front":
        if len(deque) > 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif command[0] == "pop_back":
        if len(deque) > 0:
            print(deque.pop())
        else:
            print(-1)