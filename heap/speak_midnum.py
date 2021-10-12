'''
TITLE   : 가운데를 말해요
URL     : https://www.acmicpc.net/problem/1655
DATE    : 21.10.11
'''
import sys
import heapq

n = int(sys.stdin.readline())
min_heap = []
max_heap = []

first = True
left = 0
right = 0
for i in range(n):
    num = int(sys.stdin.readline())
    # 홀수번째
    if i % 2 == 0:
        heapq.heappush(max_heap, -num)
    # 짝수번째
    else:
        heapq.heappush(min_heap, num)
    
    if len(max_heap) > 0 and len(min_heap) > 0 and -max_heap[0] > min_heap[0]:
        left = -heapq.heappop(max_heap)
        right = heapq.heappop(min_heap)
        
        heapq.heappush(max_heap, -right)
        heapq.heappush(min_heap, left)
        
    print(-max_heap[0])