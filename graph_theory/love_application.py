##### 나만 안되는 연애 #####
# URL : https://www.acmicpc.net/problem/14621
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
univ_gender = []
univ_gender = list(sys.stdin.readline().split())
univ_gender.insert(0,'-')

edges = []
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    if univ_gender[u] != univ_gender[v]:
        edges.append((d,u,v))
edges.sort()

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

# kruscal
answer = 0
cnt = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        answer += cost
        cnt += 1

# 모든 학교를 연결 했는지 확인
if cnt == n-1:
    all_connected = True
else:
    all_connected = False

if all_connected:
    print(answer)
else:
    print(-1)