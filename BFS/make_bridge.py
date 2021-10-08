'''
TITLE   : 다리 만들기
URL     : https://www.acmicpc.net/problem/2146
DATE    : 21.10.08
'''
import sys
from collections import deque
INF = 10e9

dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 섬의 가장자리에서 bfs탐색
def bfs(x, y, islands_map):
    start = islands_map[x][y]
    q = deque()
    visit = [[False]*n for _ in range(n)]
    visit[x][y] = True
    q.append((x,y,0))
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and islands_map[nx][ny] == 0:
                visit[nx][ny] = True
                q.append((nx,ny,dist+1))
            elif 0<=nx<n and 0<=ny<n and not visit[nx][ny] and islands_map[nx][ny] != 0 and islands_map[nx][ny] != start:
                return dist

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    islands_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    edges = set()
    visit = [[False]*n for _ in range(n)]
    cnt = 0
    # 모든 섬을 탐색하며 숫자 매기기 and 섬의 가장자리는 edges에 저장
    for i in range(n):
        for j in range(n):
            if visit[i][j] or islands_map[i][j] == 0:
                continue
            cnt += 1
            q = deque()
            visit[i][j] = True
            q.append((i,j))
            while q:
                x, y = q.popleft()
                islands_map[x][y] = cnt
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<n and not visit[nx][ny] and islands_map[nx][ny] == 1:
                        visit[nx][ny] = True
                        q.append((nx,ny))
                    elif 0<=nx<n and 0<=ny<n and islands_map[nx][ny] == 0:
                        edges.add((x,y))

    min_dist = INF
    for edge in edges:
        x, y = edge
        min_dist = min(min_dist, bfs(x, y, islands_map))
    print(min_dist)