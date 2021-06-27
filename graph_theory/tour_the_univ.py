##### 학교 탐방하기 #####
# URL : https://www.acmicpc.net/problem/13418
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

edges = []
for _ in range(m+1):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((c,a,b))

# 최악 경로 피로도 계산
edges.sort()

parent = list(range(n+1))

# Kruscal
cnt = 0
for edge in edges:
    c, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        if c == 0:
            cnt += 1
max_fatigue = pow(cnt,2)

# 최적 경로 피로도 계산

parent = list(range(n+1))

# Kruscal
cnt = 0
for edge in edges[::-1]:
    c, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        if c == 0:
            cnt += 1
min_fatigue = pow(cnt,2)

print(max_fatigue - min_fatigue)