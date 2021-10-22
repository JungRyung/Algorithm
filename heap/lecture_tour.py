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
before = requests[0][1]
ans = 0
for request in requests:
    q, d = request
    if before == d:
        heapq.heappush(heap, -q)
    else:
        ans += -heap[0]
        heap = []
        heapq.heappush(heap, -q)
        before = d
if heap:
    ans += -heap[0]
print(ans)