##### 네트워크 연결 #####
# URL : https://www.acmicpc.net/problem/1922
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
edges = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

edges.sort()

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

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

# Kruscal 알고리즘 시작
answer = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost

print(answer)