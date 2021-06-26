##### 우주신들과의 교감 #####
# URL : https://www.acmicpc.net/problem/1774
import sys
import math

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

n, m = map(int, sys.stdin.readline().split())
stars = [0] * (n+1)
for i in range(1,n+1):
    x, y  = map(int, sys.stdin.readline().split())
    stars[i] = (x,y)

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent,a,b)

# edges 생성
edges = []
for i in range(1,n):
    for j in range(i+1,n+1):
        x1 ,y1 = stars[i]
        x2, y2 = stars[j]
        edges.append((math.sqrt(pow(x1-x2,2)+pow(y1-y2,2)),i,j))
edges.sort()
# kruscal
answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost
print('{0:.2f}'.format(answer))