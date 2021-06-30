##### 등굣길 #####
# URL : https://programmers.co.kr/learn/courses/30/lessons/42898
dx = [0,1]
dy = [1,0]
def solution(m, n, puddles):
    answer = 0
    
    weights = [[0]*(m+1) for _ in range(n+1)]
    def move(start):
        if start in puddles:
            return
        x, y = start
        weights[x][y] += 1
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            move((nx,ny))

    

    return weights[n][m]

m, n = 4, 3
puddles = [[2, 2]]

answer = solution(m,n,puddles)
print(answer)