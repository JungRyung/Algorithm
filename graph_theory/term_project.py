'''
TITLE   : 텀 프로젝트
URL     : https://www.acmicpc.net/problem/9466
DATE    : 21.07.28
'''
import sys
sys.setrecursionlimit(100000)

def dfs(s):
    global group
    visit[s] = True
    cycle.append(s)
    next = select[s]
    if visit[next]:
        if next in cycle:
            group += cycle[cycle.index(next):]
            return
    else:
        dfs(next)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    select = [0] + list(map(int, sys.stdin.readline().split()))
    visit = [False] * (n+1)
    group = []
    
    for i in range(1, n+1):
        if not visit[i]:
            cycle = []
            dfs(i)
    print(n-len(group))