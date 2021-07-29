'''
TITLE   : 중량 제한
URL     : https://www.acmicpc.net/problem/1939
DATE    : 21.07.29
'''
import sys

def bfs(start, target, weight):
    visit = [False] * (n+1)
    q = []
    visit[start] = True
    q.append(start)
    while q:
        curr = q.pop(0)
        for node in graph[curr]:
            w, next = node
            if weight <= w and not visit[next]:
                if next == target:
                    return True
                visit[next] = True
                q.append(next)
    return False

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
max_weight = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    max_weight = max(max_weight, c)
v1, v2 = map(int, sys.stdin.readline().split())

left = 0
right = max_weight

answer = 0
while left <= right:
    mid = (left + right) // 2
    if bfs(v1, v2, mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)