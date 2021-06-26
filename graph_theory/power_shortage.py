##### 전력난 #####
# URL : https://www.acmicpc.net/problem/6497
import sys

def find_parent(parent,x):
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
while True:
    m, n = map(int, sys.stdin.readline().split())
    if m==0 and n==0:
        break
    all_cost = 0
    edges = []
    for i in range(n):
        x, y, z = map(int, sys.stdin.readline().split())
        edges.append((z,x,y))
        all_cost += z
    edges.sort()

    parent = [0] * m
    for i in range(m):
        parent[i] = i
    min_cost = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            min_cost += cost

    answer = all_cost - min_cost
    print(answer)
