'''
TITLE   : 중량 제한
URL     : https://www.acmicpc.net/problem/1939
DATE    : 21.07.29
'''
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
max_weight = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    max_weight = max(max_weight, c)
v1, v2 = map(int, sys.stdin.readline().split())

print(max_weight)