'''
TITLE   : 태상이의 훈련소 생활
URL     : https://www.acmicpc.net/problem/19951
DATE    : 21.09.13
'''
import sys

n, m = map(int, sys.stdin.readline().split())
grounds = list(map(int, sys.stdin.readline().split()))
rates = [0] * n

for _ in range(m):
    a, b, k = map(int, sys.stdin.readline().split())
    rates[a-1] += k
    if b < n:
        rates[b] -= k

rate = 0
for i in range(n):
    rate += rates[i]
    grounds[i] = str(grounds[i] + rate)
print(' '.join(grounds))