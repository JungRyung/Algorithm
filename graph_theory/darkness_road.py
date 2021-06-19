##### 어두운 길 #####
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

n, m = map(int, sys.stdin.readline().split())

parent = []
for i in range(n):
    parent.append(i)
edges = []

for i in range(m):
    a, b, dist = map(int, sys.stdin.readline().split())
    edges.append((dist,a,b))

edges.sort()
all_dist = 0
cost = 0

for edge in edges:
    dist, a, b = edge
    all_dist += dist
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        cost += dist

print(all_dist-cost)