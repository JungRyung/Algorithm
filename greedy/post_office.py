'''
TITLE   : 우체국
URL     : https://www.acmicpc.net/problem/2141
DATE    : 21.09.23
'''
import sys

n = int(sys.stdin.readline())
villages = []

cnt = 0
for _ in range(n):
    xi, ai = map(int, sys.stdin.readline().split())
    villages.append((xi,ai))
    cnt += ai
villages.sort()

if cnt % 2 != 0:
    cnt += 1
mid = cnt // 2

sum = 0
ans = 0
for village in villages:
    x, a = village
    sum += a
    if sum >= mid:
        ans = x
        break
print(ans)