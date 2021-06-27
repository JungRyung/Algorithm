##### 최소 스패닝 트리 #####
# URL : https://www.acmicpc.net/problem/1197
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

v, e = map(int, sys.stdin.readline().split())

edges = []
parent = [0] * (v+1)

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))
edges.sort()

for i in range(v+1):
    parent[i] = i

# Kruscal
answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost
print(answer)