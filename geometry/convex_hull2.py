'''
TITLE   : Convex Hull
URL     : https://www.acmicpc.net/problem/4181
DATE    : 21.09.30
'''
import sys
import math
INF = 10e9

def ccw(pointO, pointA, pointB):
    return (pointA[0]-pointO[0]) * (pointB[1]-pointO[1]) - (pointB[0]-pointO[0])*(pointA[1]-pointO[1])

# monotone chain 알고리즘
def monotoneChain(points):
    lower = []
    for point in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], point) < 0:
            lower.pop()
        lower.append(point)
    
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], point) < 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]

n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y, c = sys.stdin.readline().split()
    if c == 'Y':
        points.append((int(x),int(y)))
points.sort()

answer = monotoneChain(points)

print(len(answer))
for ans in answer:
    print(ans[0], ans[1])