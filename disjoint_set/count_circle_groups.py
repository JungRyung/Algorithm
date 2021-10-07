'''
TITLE   : Count Circle Groups
URL     : https://www.acmicpc.net/problem/10216
DATE    : 21.10.07
'''
import sys
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def can_connected(point1, point2):
    x1, y1, r1 = point1
    x2, y2, r2 = point2
    dist = (x2-x1)**2 + (y2-y1)**2
    if dist <= (r1+r2)**2:
        return True
    return False

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        x, y, r = map(int, sys.stdin.readline().split())
        points.append((x,y,r))
    
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if can_connected(points[i], points[j]):
                union_parent(parent,i,j)
    # parent = set(parent)
    # print(len(parent))
    ans = 0
    for i in range(n):
        if parent[i] == i:
            ans += 1
    print(ans)
    