'''
TITLE   : 로버트 후드
URL     : https://www.acmicpc.net/problem/9240
DATE    : 21.09.30
'''
import sys
import math
INF = 10e9

def slope(benchmark, point):
    if point[0] - benchmark[0] == 0:
        if point[1] > benchmark[1]:
            return INF
        else:
            return -INF
    else:
        return (point[1] - benchmark[1]) / (point[0] - benchmark[0])

def ccw(pointO, pointA, pointB):
    return (pointA[0]-pointO[0]) * (pointB[1]-pointO[1]) - (pointB[0]-pointO[0])*(pointA[1]-pointO[1])

def distance(pointA, pointB):
    return math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)

def ccw_4point(a, b, c, d):
    vec_ab = (b[0]-a[0], b[1]-a[1])
    vec_cd = (d[0]-c[0], d[1]-c[1])
    return vec_ab[0]*vec_cd[1] - vec_ab[1]*vec_cd[0]

n = int(sys.stdin.readline())

points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x,y))
points.sort()

benchmark = points[0]
sorted_points = sorted(points[1:], key = lambda x : (slope(benchmark, x), distance(benchmark, x)))
sorted_points.insert(0, benchmark)

convex_hull = []

if len(sorted_points) == 2:
    convex_hull.append(sorted_points[0])
    convex_hull.append(sorted_points[1])
else:
    convex_hull.append(sorted_points[0])
    convex_hull.append(sorted_points[1])
    for p in sorted_points[2:]:
        while len(convex_hull) >= 2:
            second = convex_hull.pop()
            first = convex_hull[-1]
            if ccw(first, second, p) > 0:
                convex_hull.append(second)
                break
        convex_hull.append(p)
# print(convex_hull)

# 완전 탐색
if len(convex_hull) == 2:
    print(distance(convex_hull[0], convex_hull[1]))
else:
    m = len(convex_hull)
    max_dist = 0
    for i in range(m):
        for j in range(i+1, m):
            max_dist = max(max_dist, distance(convex_hull[i], convex_hull[j]))
    print(max_dist)

# 회전하는 캘리퍼스
if len(convex_hull) == 2:
    print(distance(convex_hull[0], convex_hull[1]))
else:
    a, b, c, d = 0, 1, 1, 2
    max_dist = 0
    while True:
        line = distance(convex_hull[a],convex_hull[c])
        max_dist = max(max_dist, line)
        if ccw_4point(convex_hull[a],convex_hull[b],convex_hull[c],convex_hull[d]) > 0:
            c = (c+1) % len(convex_hull)
            d = (c+1) % len(convex_hull)
        else:
            a += 1
            if a >= len(convex_hull):
                break
            b = (a+1) % len(convex_hull)
    print(max_dist)