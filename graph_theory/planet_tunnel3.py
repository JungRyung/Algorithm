##### 행성 터널 #####
# 최소신장트리 구하기 -> Kruscal
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

n = int(sys.stdin.readline())
edges = []
parent = []
for i in range(n):
    parent.append(i)

x = []
y = []
z = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    x.append((tmp[0],i))
    y.append((tmp[1],i))
    z.append((tmp[2],i))
x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0],x[i][1],x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0],y[i][1],y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0],z[i][1],z[i+1][1]))

edges.sort()
answer = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)