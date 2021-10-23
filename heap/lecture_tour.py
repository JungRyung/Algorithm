'''
TITLE   : 순회강연
URL     : https://www.acmicpc.net/problem/2109
DATE    : 21.10.22
'''
import sys
import heapq

n = int(sys.stdin.readline())
requests = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

requests.sort(key = lambda x : x[1])

heap = []
for request in requests:
    q, d = request
    heapq.heappush(heap, q)
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))