'''
TITLE   : LCA 2
URL     : https://www.acmicpc.net/problem/11438
DATE    : 21.07.19
'''
import sys

MAX = 18

n = int(sys.stdin.readline())
adj = [[] for _ in range(n)]
parent = [[-1]*MAX for _ in range(n)]
depth = [-1] * n


s = []
visit = [False]*n
def make_tree(start):
    s.append(start)
    visit[start] = True
    while s:
        curr = s[-1]
        searched = False
        for next in adj[curr]:
            if not visit[next]:
                depth[next] = depth[curr] + 1
                parent[next][0] = curr
                visit[next] = True
                s.append(next)
                searched = True
        if not searched:
            s.pop(-1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)
    
depth[0] = 0
make_tree(0)

for j in range(MAX-1):
    for i in range(n):
        if parent[i][j] != -1:
            parent[i][j+1] = parent[parent[i][j]][j]

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a-=1
    b-=1
    if depth[a] < depth[b]:
        a, b = b, a
    diff = depth[a] - depth[b]
    i = 0
    while diff:
        if diff%2==1:
            a = parent[a][i]
        i += 1
        diff /= 2
        
    if a != b:
        for j in range(MAX-1,-1,-1):
            if parent[a][j] != parent[b][j]:
                a = parent[a][j]
                b = parent[b][j]
        lca = parent[a][0]+1
    print(lca)