'''
TITLE   : 어린 왕자
URL     : https://www.acmicpc.net/problem/1004
DATE    : 21.09.14
'''
import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    sum = 0
    for __ in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        # 해당 행성계가 점 두개를 모두 포함하거나 둘 다 포함하지 않는 경우는 진입/이탈이 이루어지지않음
        dist1 = ((cx-x1)**2 + (cy-y1)**2)**(1/2)
        dist2 = ((cx-x2)**2 + (cy-y2)**2)**(1/2)
        if (dist1 < r and dist2 > r) or (dist1 > r and dist2 < r):
            sum += 1
    print(sum)