'''
TITLE   : 맥주 마시면서 걸어가기
URL     : https://www.acmicpc.net/problem/9205
DATE    : 21.07.26
'''
import sys
INF = 10e9

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    nodes = []
    start_x, start_y = map(int, sys.stdin.readline().split())
    nodes.append((start_x, start_y))
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        nodes.append((x,y))
    end_x, end_y = map(int, sys.stdin.readline().split())
    nodes.append((end_x, end_y))
    
    graph = [[INF]*(n+2) for i in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                graph[i][j] = 0
                continue
            cost = abs(nodes[i][0]-nodes[j][0]) + abs(nodes[i][1]-nodes[j][1])
            if cost <= 1000:
                graph[i][j] = cost
    for k in range(n+2):
        for i in range(n+2):
            for j in range(n+2):
                cost = graph[i][k] + graph[k][j]
                if cost < graph[i][j]:
                    graph[i][j] = cost

    if graph[0][n+1] == INF:
        print("sad")
    else:
        print("happy")