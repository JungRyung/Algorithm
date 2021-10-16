'''
TITLE   : N 번째 큰 수
URL     : https://www.acmicpc.net/problem/2075
DATE    : 21.10.16
'''
import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    nums = list(map(int,sys.stdin.readline().split()))

    if not q: 
        for num in nums:
            heapq.heappush(q,num)
    else:
        for num in nums:
            if q[0] < num:
                heapq.heappush(q,num)
                heapq.heappop(q)

print(q[0])