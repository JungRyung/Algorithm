##### 별자리 만들기 #####
# URL : https://www.acmicpc.net/problem/4386
import sys
import math
from typing import AnyStr

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

n = int(sys.stdin.readline())
stars = []
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    stars.append((x, y))

edges = []
for i in range(n):
    for j in range(i+1,n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        dist = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
        edges.append((dist,i,j))
edges.sort()

# Kruscal
parent = [0]*n
for i in range(n):
    parent[i] = i

answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost
print(answer)