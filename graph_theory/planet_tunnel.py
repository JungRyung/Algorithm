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
planets = []
edges = []
parent = []
for i in range(n):
    parent.append(i)

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    for planet in planets:
        x1, y1, z1, num = planet
        cost = min(abs(x-x1),abs(y-y1),abs(z-z1))
        edges.append((cost,i,num))
        
    planets.append((x,y,z,i))

edges.sort()
answer = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)