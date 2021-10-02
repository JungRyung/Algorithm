'''
TITLE   : 공항
URL     : https://www.acmicpc.net/problem/10775
DATE    : 21.10.02
'''
import sys

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

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

parent = [i for i in range(g+1)]
ans = 0
for _ in range(p):
    curr = int(sys.stdin.readline())
    curr_parent = find_parent(parent, curr)
    if curr_parent == 0:
        break
    union_parent(parent, curr_parent, curr_parent - 1)
    ans += 1
print(ans)
    