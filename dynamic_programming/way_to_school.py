##### 등굣길 #####
# URL : https://programmers.co.kr/learn/courses/30/lessons/42898
dx = [0,1]
dy = [1,0]
def print_2d_arr(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()
def solution(m, n, puddles):
    answer = 0
    puddles_tuple = []
    for puddle in puddles:
        x, y = puddle
        puddles_tuple.append((x,y))
    
    weights = [[0]*(m+1) for _ in range(n+1)]
    def move(start):
        if start in puddles_tuple:
            return
        x, y = start
        weights[x][y] += 1
        print_2d_arr(weights)
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= n and ny <= m:  
                move((nx,ny))
    move((1,1))

    return weights[n][m]

m, n = 4, 3
puddles = [[2, 2]]

answer = solution(m,n,puddles)
print(answer)