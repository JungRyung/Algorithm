##### 행성 터널 #####
# 최소신장트리 구하기 -> Kruscal
import sys
import copy

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
    tmp_parent = copy.deepcopy(parent)
    x, y, z = map(int, sys.stdin.readline().split())
    tmp_edges = []
    for planet in planets:
        x1, y1, z1, num = planet
        cost = min(abs(x-x1),abs(y-y1),abs(z-z1))
        tmp_edges.append((cost,i,num))
    tmp_edges = edges + tmp_edges
    # Kruscal
    tmp_edges.sort()
    result_edges=[]
    for tmp_edge in tmp_edges:
        cost, a, b = tmp_edge
        if find_parent(tmp_parent,a) != find_parent(tmp_parent,b):
            union_parent(tmp_parent,a,b)
            result_edges.append(tmp_edge)
    edges = copy.deepcopy(result_edges)
    planets.append((x,y,z,i))

edges.sort()
answer = 0

for edge in edges:
    cost, a, b = edge
    answer += cost

print(answer)