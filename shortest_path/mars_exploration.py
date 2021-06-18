import sys
INF = int(1e9)
t = int(sys.stdin.readline())

answer = []
for _ in range(t):
    n = int(sys.stdin.readline())
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    pos = (0,0)
    mars_map = [[] for _ in range(n)]
    for i in range(n):
        mars_map[i] = list(map(int, sys.stdin.readline().split()))
    visit = [[False]*n for _ in range(n)]
    def search(visit,pos,pay):
        x, y = pos
        pay += mars_map[x][y]
        if x==n-1 and y==n-1:
            return pay
        min_dist = INF
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if visit[nx][ny] == False:
                    visit[nx][ny] = True
                    min_dist = min(min_dist, search(visit,(nx,ny),pay))
                    visit[nx][ny] = False
        return min_dist
    visit[0][0] = True
    tmp_answer = search(visit,(0,0),0)
    print(tmp_answer)
    answer.append(tmp_answer)
print(answer)