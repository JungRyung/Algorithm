'''
TITLE   : 케빈베이컨의 6단계 법칙
URL     : https://www.acmicpc.net/problem/1389
DATE    : 21.07.26
'''
import sys
INF = 10e9

n, m = map(int, sys.stdin.readline().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                graph[i][j] = 0
                continue
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

num_of_kevin = [0] * (n+1)
for i in range(1,n+1):
    num_of_kevin[i] = sum(graph[i][1:])

min_num = INF
answer = 0
for i in range(1,n+1):
    if num_of_kevin[i] < min_num:
        min_num = num_of_kevin[i]
        answer = i
print(answer)