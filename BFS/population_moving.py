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
    sum = country_map[x][y]
    num = 1
    united = []
    united.append((x,y))
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
                    united.append((nx,ny))
                    visit[nx][ny] = cnt
                    sum += country_map[nx][ny]
                    num += 1
    for i, j in united:
        country_map[i][j] = sum//num
            
    return changed, visit

def print_map(tmp_map):
    for i in range(n):
        for j in range(n):
            print(tmp_map[i][j],end=' ')
        print()
    
t = 0
while 1:
    visit = [[0]*n for _ in range(n)]
    # print(visit)
    cnt = 1
    # 연합 결성
    changed = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                tmp_flag, visit = bfs(i,j,visit,cnt)
                if changed == True and tmp_flag == False:
                    changed = True
                else:
                    changed = tmp_flag
                cnt += 1
            
    if changed == True:
        # 인구 이동
        # pop_sum = [[0,0] for _ in range(cnt)]
        # for i in range(1,cnt):
        #     pop_sum.append([0,0])
        # for i in range(n):
        #     for j in range(n):
        #         idx = visit[i][j]
        #         pop_sum[idx][0] += country_map[i][j]
        #         pop_sum[idx][1] += 1
        # avg = [0] * cnt
        # for i in range(1,cnt):
        #     avg[i] = int(pop_sum[i][0] / pop_sum[i][1])
        # for i in range(n):
        #     for j in range(n):
        #         if visit[i][j] != 0:
        #             country_map[i][j] = avg[visit[i][j]]
        # print_map(country_map)
        t += 1
    else:
        print(t)
        break