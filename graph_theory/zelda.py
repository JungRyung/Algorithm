'''
TITLE   : 녹색 옷 입은 애가 젤다지?
URL     : https://www.acmicpc.net/problem/4485
DATE    : 21.07.26
'''
import sys
import heapq
INF = 10e9

dx = [-1,0,1,0]
dy = [0,-1,0,1]

step = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cave = [[] for _ in range(n)]
    res = [[INF]*n for _ in range(n)]
    for i in range(n):
        cave[i] = list(map(int, sys.stdin.readline().split()))
    
    visit = [[False]*n for _ in range(n)]
    q = []
    res[0][0] = cave[0][0]
    heapq.heappush(q, (res[0][0],0,0))
    while q:
        curr = heapq.heappop(q)
        for i in range(4):
            nx = curr[1] + dx[i]
            ny = curr[2] + dy[i]
            if 0<=nx<n and 0<=ny<n:
                nw = curr[0] + cave[nx][ny]
                if res[nx][ny] > nw:
                    res[nx][ny] = nw
                    heapq.heappush(q, (nw,nx,ny))
        
    print("Problem {0}: {1}".format(step,res[n-1][n-1]))
    step += 1