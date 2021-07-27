'''
TITLE   : 아기 상어
URL     : https://www.acmicpc.net/problem/16236
DATE    : 21.07.26
'''
import sys
import heapq

dx = [-1,0,0,1]
dy = [0,-1,1,0]

class baby_shark:
    def __init__(self):
        self.size = 2
        self.pos = (0, 0)
        self.eat_cnt = 0
        self.time = 0
    def get_size(self):
        return self.size
    def set_size(self, size):
        self.size = size
    def get_pos(self):
        return self.pos
    def set_pos(self, x, y):
        self.pos = (x, y)
    def get_time(self):
        return self.time
    def plus_time(self,time):
        self.time += time
    def eat_feed(self):
        self.eat_cnt += 1
        if self.eat_cnt == self.size:
            self.size += 1
            self.eat_cnt = 0
        
n = int(sys.stdin.readline())
area = [[]*n for _ in range(n)]
shark = baby_shark()
for i in range(n):
    area[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if area[i][j] == 9:
            shark.set_pos(i,j)

def search_feed(pos):
    x, y = pos
    area[x][y] = 0
    q = []
    visit = [[False]*n for _ in range(n)]
    heapq.heappush(q,(0,x,y))
    visit[x][y] = True
    while q:
        time, curr_x, curr_y  = heapq.heappop(q)
        if 0 < area[curr_x][curr_y] < shark.get_size():
            area[curr_x][curr_y] = 9
            shark.eat_feed()
            shark.plus_time(time)
            shark.set_pos(curr_x,curr_y)
            return True
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0<=nx<n and 0<=ny<n and area[nx][ny] <= shark.get_size() and not visit[nx][ny]:
                visit[nx][ny] = True
                heapq.heappush(q,(time+1,nx,ny))
    return False

while True:
    if not search_feed(shark.get_pos()):
        print(shark.get_time())
        break