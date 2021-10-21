'''
TITLE   : 중앙값 구하기
URL     : https://www.acmicpc.net/problem/2696
DATE    : 21.10.21
'''
import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    m = int(sys.stdin.readline())
    nums = []
    for __ in range(m // 10 + 1):
        nums += list(map(int, sys.stdin.readline().split()))
    min_heap = []
    max_heap = []
    ans = []
    for i in range(m):
        num = nums[i]
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
        if i % 2 == 0:
            ans.append(str(-max_heap[0]))
    ans_length = len(ans)
    print(ans_length)
    for i in range(ans_length // 10 + 1):
        if i == ans_length // 10:
            print(' '.join(ans[i*10:]))
        else:
            print(' '.join(ans[i*10:i*10+10]))