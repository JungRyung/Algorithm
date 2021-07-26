'''
TITLE   : 게임 개발
URL     : https://www.acmicpc.net/problem/1516
DATE    : 21.07.26
'''
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
inDegree = [0] * (n+1)
cost = [0] * (n+1)
time = [0] * (n+1)
for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    cost[i] = tmp[0]
    for j in tmp[1:-1]:
        graph[j].append(i)
        inDegree[i] += 1

q = []
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)
        time[i] = cost[i]

while q:
    curr = q.pop(0)
    for next in graph[curr]:
        inDegree[next] -= 1
        time[next] = max(time[next], cost[next] + time[curr])
        if inDegree[next] == 0:
            q.append(next)

for i in range(1,n+1):
    print(time[i])