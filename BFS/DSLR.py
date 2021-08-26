'''
TITLE   : DSLR
URL     : https://www.acmicpc.net/problem/9019
DATE    : 21.08.24
'''
import sys
from collections import deque

def double(num):
    return num*2 % 10000
    
def sub(num):
    if num == 0:
        return 9999
    else:
        return num -1
    
def round_R(num):
    next = num // 10
    next += (num % 10) * 1000
    return next 

def round_L(num):
    if num<1000:
        return 10*num
    else:
        next = (num % 1000) * 10
        next += num // 1000
        return next

def bfs(a,b):
    visit = [False]*10000
    visit[a] = True
    q = deque()
    q.append((a,''))
    while q:
        curr, command = q.popleft()
        if curr == b:
            return command
        next = double(curr)
        if not visit[next]:
            visit[next] = True
            q.append((next,command+'D'))
        next = sub(curr)
        if not visit[next]:
            visit[next] = True
            q.append((next,command+'S'))
        next = round_L(curr)
        if not visit[next]:
            visit[next] = True
            q.append((next,command+'L'))
        next = round_R(curr)
        if not visit[next]:
            visit[next] = True
            q.append((next,command+'R'))

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a,b))