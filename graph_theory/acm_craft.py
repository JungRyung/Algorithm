'''
TITLE   : ACM Craft
URL     : https://www.acmicpc.net/problem/1005
DATE    : 21.09.09
'''
import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n, k = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for __ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(sys.stdin.readline())
    dp = [0] * (n+1)
    
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    while q:
        curr = q.popleft()
        for next in graph[curr]:
            if dp[next] < dp[curr] + time[next]:
                dp[next] = dp[curr] + time[next]
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    print(dp[w])