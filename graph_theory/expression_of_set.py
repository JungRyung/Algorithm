'''
TITLE   : 집합의 표현
URL     : https://www.acmicpc.net/problem/1717
DATE    : 21.09.09
'''
import sys
sys.setrecursionlimit(100000)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")