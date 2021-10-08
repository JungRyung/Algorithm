'''
TITLE   : 숨바꼭질 4
URL     : https://www.acmicpc.net/problem/13913
DATE    : 21.10.08
'''
import sys
from collections import deque
MAX = 100000

n, k = map(int, sys.stdin.readline().split())

visit = [False] * (MAX+1)
time = [0] * (MAX+1)
from_list = [i for i in range(MAX+1)]

q = deque()
q.append(n)
visit[n] = True

while q:
    curr = q.popleft()
    if curr * 2 <= MAX and not visit[curr*2]:
        visit[curr*2] = True
        time[curr*2] = time[curr] + 1
        from_list[curr*2] = curr
        q.append(curr*2)
    if (curr + 1) <= MAX and not visit[curr+1]:
        visit[curr+1] = True
        time[curr+1] = time[curr] + 1
        from_list[curr+1] = curr
        q.append(curr+1)
    if (curr - 1) >= 0 and not visit[curr-1]:
        visit[curr-1] = True
        time[curr-1] = time[curr] + 1
        from_list[curr-1] = curr
        q.append(curr-1)

print(time[k])

route = []
route.append(str(k))
while from_list[k] != k:
    route.append(str(from_list[k]))
    k = from_list[k]
print(' '.join(route[::-1]))