'''
TITLE   : 거짓말
URL     : https://www.acmicpc.net/problem/1043
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

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]
tmp_list = list(map(int, sys.stdin.readline().split()))
knows = []
knows_len = tmp_list[0]
if knows_len > 0:
    knows = tmp_list[1:]

if knows_len > 1:
    for i in range(knows_len - 1):
        union_parent(parent, knows[i], knows[i+1])

partys = []
for _ in range(m):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    num = tmp_list[0]
    party = tmp_list[1:]
    if num > 1:
        for i in range(num-1):
            union_parent(parent, party[i], party[i+1])
    partys.append(party)
if knows_len == 0:
    print(len(partys))
else:
    ans = 0
    for party in partys:
        if find_parent(parent, knows[0]) != find_parent(parent, party[0]):
            ans += 1
    print(ans)