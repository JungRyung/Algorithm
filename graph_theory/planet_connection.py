##### 행성 연결 #####
# URL : https://www.acmicpc.net/problem/16398
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
adjacent_list = [[] for _ in range(n)]
for i in range(n):
    adjacent_list[i] = list(map(int, sys.stdin.readline().split()))

edges = []
for i in range(n):
    for j in range(i+1):
        if adjacent_list != 0:
            edges.append((adjacent_list[i][j],i,j))
edges.sort()

parent = [0] * n
for i in range(n):
    parent[i] = i

# kruscal
answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)