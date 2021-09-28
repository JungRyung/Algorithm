'''
TITLE   : 볼록 껍질
URL     : https://www.acmicpc.net/problem/1708
DATE    : 21.09.28
'''
import sys
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
ccw_sort.sort()

stack = []
stack.append(benchmark)
stack.append((ccw_sort[0][1], ccw_sort[0][2]))
ccw_sort.pop(0)

for point in ccw_sort:
    x, y = point[1], point[2]
    while len(stack) >= 2:
        tmp_ccw = ccw(stack[-2], stack[-1], (x,y))
        if tmp_ccw < 0:
            stack.pop()
        else:
            break
    tmp_ccw = ccw(stack[-2], stack[-1], (x,y))
    if tmp_ccw > 0:
        stack.append((x,y))
    elif tmp_ccw == 0:
        a, b = dist(stack[-2],stack[-1],(x,y))
        if b > a:
            stack.pop()
            stack.append((x,y))
print(len(stack))