'''
TITLE   : 강의실 배정
URL     : https://www.acmicpc.net/problem/11000
DATE    : 21.10.16
'''
import sys
import heapq

n = int(sys.stdin.readline())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
times.sort(key= lambda x: x[0])

q = []
heapq.heappush(q, times[0][1])

for i in range(1,n):
    if q[0] <= times[i][0]:
        heapq.heappop(q)
    heapq.heappush(q, times[i][1])
print(len(q))