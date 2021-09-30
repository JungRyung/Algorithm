'''
TITLE   : 로버트 후드
URL     : https://www.acmicpc.net/problem/9240
DATE    : 21.09.28
'''
import sys
import math
INF = 10e9

def slope(benchmark, point):
    if point[0] - benchmark[0] == 0:
        if point[1] - benchmark[1] > 0:
            return INF
        else:
            return -INF
    else:       
        return (point[1] - benchmark[1]) / (point[0] - benchmark[0])

def ccw(pointO, pointA, pointB):
    return (pointA[0]-pointO[0])*(pointB[1]-pointO[1]) - (pointB[0]-pointO[0])*(pointA[1]-pointO[1])

def dist(pointO, pointA, pointB):
    distA = (pointA[0]-pointO[0])**2 + (pointA[1]-pointO[1])**2
    distB = (pointB[0]-pointO[0])**2 + (pointB[1]-pointO[1])**2
    return distA, distB

def distance(pointA, pointB):
    return math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)

def ccw_4point(a, b, c, d):
    vec_ab = (b[0]-a[0], b[1]-a[1])
    vec_cd = (d[0]-c[0], d[1]-c[1])
    return vec_ab[0]*vec_cd[1] - vec_ab[1]*vec_cd[0]

n = int(sys.stdin.readline())

points = []
min_x = INF
benchmark = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x < min_x:
        benchmark = (x,y)
        min_x = x
    elif x == min_x:
        if y < benchmark[1]:
            benchmark = (x,y)
            min_x = x
    points.append((x,y))

ccw_sort = []
for point in points:
    if benchmark == point:
        continue
    x, y = point
    ccw_sort.append((slope(benchmark, point), x, y))
# ccw_sort.sort()
ccw_sort = sorted(ccw_sort, key = lambda x : (x[0], distance(benchmark,(x[1],x[2]))))

convex_hull = []
convex_hull.insert(0, benchmark)
convex_hull.append((ccw_sort[0][1], ccw_sort[0][2]))
ccw_sort.pop(0)

print(ccw_sort)

for point in ccw_sort:
    x, y = point[1], point[2]
    while len(convex_hull) >= 2:
        second = convex_hull[-1]
        convex_hull.pop()
        first = convex_hull[-1]
        if ccw(first, second, (x,y)) > 0:
            convex_hull.append(second)
            break
    convex_hull.append((x,y))
print(convex_hull)
            


# for point in ccw_sort:
#     x, y = point[1], point[2]
#     while len(convex_hull) >= 2:
#         tmp_ccw = ccw(convex_hull[-2], convex_hull[-1], (x,y))
#         if tmp_ccw < 0:
#             convex_hull.pop()
#         else:
#             break
#     if len(convex_hull) < 2:
#         convex_hull.append((x,y))
#     else:
#         tmp_ccw = ccw(convex_hull[-2], convex_hull[-1], (x,y))
#         if tmp_ccw > 0:
#             convex_hull.append((x,y))
#         elif tmp_ccw == 0:
#             a, b = dist(convex_hull[-2],convex_hull[-1],(x,y))
#             if b > a:
#                 convex_hull.pop()
#                 convex_hull.append((x,y))

# 회전하는 캘리퍼스
if len(convex_hull) == 2:
    print(math.sqrt((convex_hull[0][0]-convex_hull[1][0])**2 + (convex_hull[0][1]-convex_hull[1][1])**2))
elif len(convex_hull) > 2:
    m = len(convex_hull)
    max_dist = 0
    for i in range(m):
        for j in range(i+1,m):
            max_dist = max(max_dist, distance(convex_hull[i], convex_hull[j]))
    # a, b, c, d = 0, 1, 1, 2
    # max_dist = 0
    # while True:
    #     print(a,b,c,d)
    #     line = distance(convex_hull[a],convex_hull[c])
    #     max_dist = max(max_dist, line)
    #     if ccw_4point(convex_hull[a],convex_hull[b],convex_hull[c],convex_hull[d]) > 0:
    #         c = (c+1) % len(convex_hull)
    #         d = (c+1) % len(convex_hull)
    #     else:
    #         a += 1
    #         if a >= len(convex_hull):
    #             break
    #         b = (a+1) % len(convex_hull)
    print(max_dist)
