'''
Title   : 여행 가자
URL     : https://www.acmicpc.net/problem/1976
DATE    : 21.07.25
'''
import sys

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [0] * n
for i in range(n):
    parent[i] = i

for i in range(n):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if tmp_list[j] == 1:
            union_parent(parent,i,j)
plan = list(map(int, sys.stdin.readline().split()))
ac = find_parent(parent, plan[0]-1)
possible = True
for city in plan:
    if ac!= find_parent(parent, city-1):
        possible = False
        break
if possible:
    print("YES")
else:
    print("NO")