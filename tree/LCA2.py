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

def make_tree(curr):
    for next in adj[curr]:
        if(depth[next] == -1):
            depth[next] = depth[curr] + 1
            parent[next][0] = curr
            make_tree(next)

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
    if depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a, b = b, a
        for i in range(MAX-1,-1,-1):
            if depth[a] <= depth[parent[b][i]]:
                b = parent[b][i]
        
    if a != b:
        for i in range(MAX-1,-1,-1):
            if parent[a][i] != -1 and parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
        lca = parent[a][0]+1
    print(lca)