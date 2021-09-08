'''
TITLE   : 알파벳
URL     : https://www.acmicpc.net/problem/1987
DATE    : 21.09.08
'''
import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

r, c = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().strip()) for _ in range(r)]
# visit = [False] * 26
visited = set()
longest = 0

def bfs():
    q = deque()
    visited.add(board[0][0])
    q.append((0,0,1))
    while q:
        x, y, t, visited = q.popleft()
        print(t)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in visited:
                visited.add(board[nx][ny])
                q.append((nx,ny,t+1,visited))


# def dfs_stack():
#     s = []
#     s.append((0,0,1))
#     longest = 0
#     while s:
#         x, y, t = s[-1]
#         longest = max(longest,t)
#         visit[ord(board[x][y])-65] = True
#         searched = False
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<r and 0<=ny<c and not visit[ord(board[nx][ny])-65]:
#                 s.append((nx,ny,t+1))
#                 searched = True
#                 break
#         if not searched:
#             s.pop()
#     return longest

# def dfs(x,y,t):
#     global longest
#     longest = max(longest,t)
#     visit[ord(board[x][y])-65] = True
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<r and 0<=ny<c and not visit[ord(board[nx][ny])-65]:
#             dfs(nx,ny,t+1)
#     visit[ord(board[x][y])-65] = False
