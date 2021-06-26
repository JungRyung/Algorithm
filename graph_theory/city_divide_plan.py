##### 도시 분할 계획 #####
# URL : https://www.acmicpc.net/problem/1647
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())

edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

edges.sort()

# Kruscal
answer = 0
max_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost
        max_cost = max(max_cost,cost)

print(answer-max_cost)