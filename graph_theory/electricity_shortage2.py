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

# 세 개의 발전소를 union하고 그 후 kruscal을 돌리면 해결 됨
for i in range(k-1):
    union_parent(parent,power_plants[i],power_plants[i+1])

# Kruscal
answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost
print(answer)