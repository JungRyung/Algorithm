'''
TITLE   : 고속도로
URL     : https://www.acmicpc.net/problem/10254
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

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())

    points = []
    for __ in range(n):
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

    # 회전하는 캘리퍼스
    if len(convex_hull) == 2:
        print(convex_hull[0][0],convex_hull[0][1],convex_hull[1][0],convex_hull[1][1])
    else:
        a, b, c, d = 0, 1, 1, 2
        max_dist = 0
        x1, y1, x2, y2 = 0, 0, 0, 0
        while True:
            line = distance(convex_hull[a],convex_hull[c])
            if line > max_dist:
                max_dist = line
                x1, y1, x2, y2 = convex_hull[a][0], convex_hull[a][1], convex_hull[c][0], convex_hull[c][1]
            
            if ccw_4point(convex_hull[a],convex_hull[b],convex_hull[c],convex_hull[d]) > 0:
                c = (c+1) % len(convex_hull)
                d = (c+1) % len(convex_hull)
            else:
                a += 1
                if a >= len(convex_hull):
                    break
                b = (a+1) % len(convex_hull)
        print(x1, y1, x2, y2)