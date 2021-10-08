'''
TITLE   : 트리
URL     : https://www.acmicpc.net/problem/4803
DATE    : 21.10.08
'''
import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, is_cycle, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        if is_cycle[b]:
            is_cycle[a] = True
        parent[b] = a
    else:
        parent[a] = b

case_cnt = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n==0 and m==0:
        break

    parent = [i for i in range(n+1)]
    is_cycle = [False] * (n+1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        if find_parent(parent,a) == find_parent(parent,b):
            is_cycle[find_parent(parent,a)] = True
        else:
            union_parent(parent,is_cycle,a,b)
    
    cnt = 0
    for i in range(1,n+1):
        if parent[i] == i and not is_cycle[i]:
            cnt += 1
    
    if cnt == 0:
        print("case ",case_cnt,": No trees.",sep='')
    elif cnt == 1:
        print("case ",case_cnt,": There is one tree.",sep='')
    else:
        print("case ",case_cnt,": A forest of ",cnt," trees.",sep='')
    case_cnt += 1