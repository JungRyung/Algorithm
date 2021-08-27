'''
TITLE   : 트리의 지름
URL     : https://www.acmicpc.net/problem/1167
DATE    : 21.08.26
'''
import sys
from collections import deque

v = int(sys.stdin.readline())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    inform = list(map(int, sys.stdin.readline().split()))
    vnum = inform[0]
    inform = inform[1:-1]
    num = len(inform) // 2
    for i in range(num):
        b, cost = inform[2*i], inform[2*i+1]
        tree[vnum].append((b,cost))

def dfs(start):
    visit = [False] * (v+1)
    s = []
    s.append((start, 0))
    max_dist = 0
    max_node = 0
    while s:
        curr, dist = s[-1]
        visit[curr] = True
        searched = False
        for next in tree[curr]:
            next_node, cost = next
            if not visit[next_node]:
                if max_dist < dist + cost:
                    max_dist = dist + cost
                    max_node = next_node
                s.append((next_node, dist + cost))
                searched = True
                break
        if not searched:
            s.pop(-1)
    return max_node, max_dist

def bfs(start):
    visit = [False] * (v+1)
    q = deque()
    q.append((start, 0))
    visit[start] = True
    max_dist = 0
    max_node = 0
    while q:
        curr, dist = q.popleft()
        for next in tree[curr]:
            next_node, cost = next
            if not visit[next_node]:
                if max_dist < dist + cost:
                    max_dist = dist + cost
                    max_node = next_node
                visit[next_node] = True
                q.append((next_node, dist + cost))
    return max_node, max_dist

next, dist = bfs(1)
next, dist = bfs(next)
        
print(dist)
