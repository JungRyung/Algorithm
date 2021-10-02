'''
TITLE   : 친구비
URL     : https://www.acmicpc.net/problem/16562
DATE    : 21.10.02
'''
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, costs, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if costs[a] < costs[b]:
        parent[b] = a
    elif costs[a] == costs[b]:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    else:
        parent[a] = b

n, m, k = map(int, sys.stdin.readline().split())
costs = [0] + list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, costs, a, b)

min_cost = 0
for i in range(1,n+1):
    # root인 경우만 계산
    if i == parent[i]:
        min_cost += costs[i]

if min_cost <= k:
    print(min_cost)
else:
    print("Oh no")