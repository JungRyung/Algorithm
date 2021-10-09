'''
TITLE   : 트리
URL     : https://www.acmicpc.net/problem/4803
DATE    : 21.10.08
'''
import sys
from collections import deque

def bfs():
    total = 0
    is_tree = True

    for i in range(1,n+1):
        if not visit[i]:
            is_tree = True
            visit[i] = True
            q.append(i)
    
            while q:
                curr = q.popleft()
                for next in graph[curr]:
                    if visit[next] and parent[curr]!=next:
                        is_tree = False
                    elif visit[next]:
                        continue
                    else:
                        visit[next] = True
                        parent[next] = curr
                        q.append(next)
            if is_tree:
                total += 1
    return total



case_cnt = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n==0 and m==0:
        break
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    visit = [False] * (n+1)
    parent = [0] * (n+1)
    q = deque()

    cnt = bfs()

    if cnt == 0:
        print("case ",case_cnt,": No trees.",sep='')
    elif cnt == 1:
        print("case ",case_cnt,": There is one tree.",sep='')
    else:
        print("case ",case_cnt,": A forest of ",cnt," trees.",sep='')
    case_cnt += 1