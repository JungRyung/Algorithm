from collections import deque

n, k = map(int, input().split())
virus_map = [[] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 시험관의 정보 입력 받기
for i in range(n):
    virus_map[i] = list(map(int, input().split()))

virus = []
# 바이러스가 어디에 위치하는지 확인
for i in range(n):
    for j in range(n):
        if virus_map[i][j] != 0:
            virus.append((virus_map[i][j],i,j,0))
virus.sort()

s, x, y = map(int, input().split())

q = deque(virus)    # 초기 바이러스의 정보를 큐에 삽입

while q:
    v, tmpX, tmpY, t = q.popleft()
    if t == s:
        break
    for i in range(4):
        nx = tmpX + dx[i]
        ny = tmpY + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<n:
            if virus_map[nx][ny] == 0:
                virus_map[nx][ny] = v
                q.append((v, nx, ny, t+1))

print(virus_map[x-1][y-1])
    