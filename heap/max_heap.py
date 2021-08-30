'''
TITLE   : 최대 힙
URL     : https://www.acmicpc.net/problem/11279
DATE    : 21.08.30
'''
import sys
import heapq

q = []
n = int(sys.stdin.readline())
for _ in range(n):
    input = int(sys.stdin.readline())
    if input > 0:
        heapq.heappush(q, -input)
    else:
        if len(q) > 0:
            print(-heapq.heappop(q))
        else:
            print(0)