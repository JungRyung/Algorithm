'''
TITLE   : 소수의 곱
URL     : https://www.acmicpc.net/problem/2014
DATE    : 21.10.19
'''
import sys
import heapq

k, n = map(int, sys.stdin.readline().split())
primes = list(map(int, sys.stdin.readline().split()))

ans = list(primes)
heapq.heapify(ans)
for _ in range(n):
    front = heapq.heappop(ans)
    for p in primes:
        heapq.heappush(ans, front*p)
        if front % p == 0:
            break
print(front)