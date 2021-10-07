'''
TITLE   : 선분 그룹
URL     : https://www.acmicpc.net/problem/2162
DATE    : 21.10.07
'''
import sys
sys.setrecursionlimit(10**6)

def ccw(pointO, pointA, pointB):
    tmp = (pointA[0]-pointO[0])*(pointB[1]-pointO[1]) - (pointB[0]-pointO[0])*(pointA[1]-pointO[1])
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

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
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a == b:
        return
    elif a < b:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b

n = int(sys.stdin.readline())
parent = [-1 for i in range(n)]

# segments = []
# for i in range(n):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     for index, segment in enumerate(segments):
#         if is_intersect((segment[0],segment[1]),(segment[2],segment[3]),(x1,y1),(x2,y2)):
#             union_parent(parent,index,i)
#     segments.append((x1, y1, x2, y2))

segments = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        pointA = (segments[i][0],segments[i][1])
        pointB = (segments[i][2],segments[i][3])
        pointC = (segments[j][0],segments[j][1])
        pointD = (segments[j][2],segments[j][3])
        if is_intersect(pointA,pointB,pointC,pointD):
            union_parent(parent,i,j)
cnt = 0
maxVal = 0
for i in range(n):
    if parent[i] < 0:
        cnt += 1
        maxVal = max(maxVal, abs(parent[i]))
print(cnt)
print(maxVal)