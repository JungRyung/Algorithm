'''
TITLE   : Convex Hull
URL     : https://www.acmicpc.net/problem/4181
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

def compare(benchmark, point):
    if slope(benchmark,point) > 0:
        

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y, c = sys.stdin.readline().split()
    if c == 'Y':
        points.append((int(x),int(y)))
points.sort()

benchmark = points[0]
sorted_points = sorted(points[1:], key = lambda x : (slope(benchmark, x), distance(benchmark, x)))
sorted_points.insert(0, benchmark)

convex_hull = []
convex_hull.append(sorted_points[0])
convex_hull.append(sorted_points[1])
for p in sorted_points[2:]:
    while len(convex_hull) >= 2:
        second = convex_hull.pop()
        first = convex_hull[-1]
        if ccw(first, second, p) >= 0:
            convex_hull.append(second)
            break
    convex_hull.append(p)

print(len(convex_hull))
for point in convex_hull:
    print(point[0],point[1])