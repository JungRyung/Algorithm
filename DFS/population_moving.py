# 인구 이동 url: www.acmicpc.net/problem/16234
from collections import deque
n, l, r = map(int,input().split())
country_map = [[] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in range(n):
    country_map[i] = list(map(int,input().split()))

def bfs(x,y,visit,cnt):
    q = deque()
    q.append((x,y))
    visit[x][y] = cnt
    changed = False
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
                diff = abs(country_map[tmp[0]][tmp[1]] - country_map[nx][ny])
                if diff >= l and diff <= r and visit[nx][ny] == 0:
                    changed = True
                    q.append((nx,ny))
                    visit[nx][ny] = cnt
    return changed, visit


    

flag = True
t = 0
while flag:
    visit = [[0]*n for _ in range(n)]
    # print(visit)
    cnt = 1
    # 연합 결성
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                flag, visit = bfs(i,j,visit,cnt)
                cnt += 1
            
    if flag == True:
        # 인구 이동
        pop_sum = [[0,0]]*cnt
        # for i in range(1,cnt):
        #     pop_sum.append([0,0])
        for i in range(n):
            for j in range(n):
                pop_sum[visit[i][j]][0] += country_map[i][j]
                pop_sum[visit[i][j]][1] += 1
        avg = [0] * cnt
        for i in range(1,cnt):
            avg[i] = int(pop_sum[i][0] / pop_sum[i][1])
        for i in range(n):
            for j in range(n):
                if visit[i][j] != 0:
                    country_map[i][j] = avg[visit[i][j]]
        t += 1
    else:
        print(t)
        break