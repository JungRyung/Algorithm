'''
TITLE   : 랜선 자르기
URL     : https://www.acmicpc.net/problem/1654
DATE    : 21.07.28
'''
import sys

def cable_cutting(cables, l):
    if l == 0:
        l = 1
    res = 0
    for cable in cables:
        res += cable // l
    return res

k, n = map(int, sys.stdin.readline().split())
cables = []
for _ in range(k):
    cables.append(int(sys.stdin.readline()))


left = 0
right = max(cables)
max_l = 0
while left <= right:
    mid = (left + right) // 2
    num = cable_cutting(cables, mid)
    if num >= n:
        max_l = mid
        left = mid + 1
    else:
        right = mid -1
print(max_l)