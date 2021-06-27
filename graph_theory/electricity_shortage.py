##### 전기가 부족해 #####
# URL : https://www.acmicpc.net/problem/10423
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a in power_plants or b in power_plants:
        if a in power_plants:
            parent[b] = a
        else:
            parent[a] = b
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
n, m, k= map(int, sys.stdin.readline().split())
power_plants = list(map(int, sys.stdin.readline().split()))

edges = []
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    edges.append((w,u,v))
edges.sort()

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

# Kruscal
answer = 0
for edge in edges:
    cost, a, b = edge
    parent_of_a = find_parent(parent,a)
    parent_of_b = find_parent(parent,b)
    if find_parent(parent,a) != find_parent(parent,b) and not(parent_of_a in power_plants and parent_of_b in power_plants):
        union_parent(parent,a,b)
        answer += cost
print(answer)