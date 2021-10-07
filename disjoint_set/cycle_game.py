'''
TITLE   : 사이클 게임
URL     : https://www.acmicpc.net/problem/20040
DATE    : 21.10.07
'''
import sys
sys.setrecursionlimit(10**6)

def ccw(pointO, pointA, pointB):
    return (pointA[0]-pointO[0])*(pointB[1]-pointO[1]) - (pointB[0]-pointO[0])*(pointA[1]-pointO[1])

def is_intersect(pointA, pointB, pointC, pointD):
    ab = ccw(pointA, pointB, pointC)*ccw(pointA, pointB, pointD)
    cd = ccw(pointC, pointD, pointA)*ccw(pointC, pointD, pointB)
    if ab == 0 and cd == 0:
        if pointA > pointB:
            pointA, pointB = pointB, pointA
        if pointC > pointD:
            pointC, pointD = pointD, pointC
        return pointC <= pointB and pointA <= pointD
    return ab <= 0 and cd <= 0

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
parent = [i for i in range(n)]

ans = 0
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        ans = i + 1
        break
print(ans)