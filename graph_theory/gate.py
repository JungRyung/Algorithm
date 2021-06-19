##### 탑승구 #####
import sys

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
gis = []

parent = []
for i in range(g+1):
    parent.append(i)
for i in range(p):
    gis.append(int(sys.stdin.readline()))
answer = 0
for gi in gis:
    current = gi
    cur_parent = find_parent(parent,current)
    if cur_parent == 0:
        break
    else:
        answer += 1
        union_parent(parent,cur_parent,cur_parent-1)

print(answer)