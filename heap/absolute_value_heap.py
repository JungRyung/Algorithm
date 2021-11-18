'''
TITLE   : 절댓값 힙
URL     : https://www.acmicpc.net/problem/11286
DATE    : 21.11.18
'''
import sys
import heapq

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        if command < 0:
            heapq.heappush(q, (-command, command))
        else:
            heapq.heappush(q, (command, command))
