'''
TITLE   : 탑
URL     : https://www.acmicpc.net/problem/2493
DATE    : 21.09.09
'''
import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

ans = []
s = []
for tower in enumerate(towers):
    order, height = tower
    while s:
        o, h = s[-1]
        if h < height:
            s.pop()
        else:
            ans.append(str(o+1))
            s.append(tower)
            break
    if not s:
        s.append(tower)
        ans.append('0')
print(' '.join(ans))
    