from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
lab_map = [[] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    lab_map[i] = list(map(int, input().split()))
    
blank_list = []
virus_list = []
for i in range(n):
    for j in range(m):
        if lab_map[i][j] == 0:
            blank_list.append((i,j))
        elif lab_map[i][j] == 2:
            virus_list.append((i,j))
            
def BFS(temp_map, x, y):
    q = deque()
    q.append((x,y))
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]
            if nx >=0 and nx<n and ny >=0 and ny < m:
                if temp_map[nx][ny] == 0:
                    temp_map[nx][ny] = 2
                    q.append((nx,ny))

def print_map(temp_map):
    for i in range(n):
        for j in range(m):
            print(temp_map[i][j],end=' ')
        print()

blank_coms = list(combinations(blank_list,3))
# print(blank_coms)
max_blanck = 0
for blank_com in blank_coms:
    tmp_map = copy.deepcopy(lab_map)
    for i in range(3):
        tmp_map[blank_com[i][0]][blank_com[i][1]] = 1
    # visit = [[-1]*m for _ in range(n)]
    for virus in virus_list:
        BFS(tmp_map, virus[0],virus[1])
    # 안전구역 개수 구하기
    cnt = 0
    for i in range(n):
        cnt += tmp_map[i].count(0)
    max_blanck = max(max_blanck, cnt)
# print_map(lab_map)
print(max_blanck)
