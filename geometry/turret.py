'''
TITLE   : 터렛
URL     : https://www.acmicpc.net/problem/1002
DATE    : 21.09.14
'''
import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    dists = [r1,r2,dist]
    max_dist = max(dists)
    dists.remove(max_dist)
    # 두 원의 중심이 다를 때
    if dist > 0:
        if max_dist > sum(dists):
            print(0)
        elif max_dist == sum(dists):
            print(1)
        else:
            print(2)
    # 두 원의 중심이 같을 때
    elif dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)