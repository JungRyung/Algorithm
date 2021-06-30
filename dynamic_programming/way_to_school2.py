##### 등굣길 #####
# URL : https://programmers.co.kr/learn/courses/30/lessons/42898
def print_2d_arr(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=' ')
        print()
def solution(n, m, puddles):
    da = [[0]*(m+1) for _ in range(n+1)]
    da[0][1] = 1
    for puddle in puddles:
        x, y = puddle
        da[x][y] = -1
    print_2d_arr(da)
    for i in range(1,n+1):
        for j in range(1,m+1):
            if da[i][j] != -1:
                left = da[i][j-1]
                up = da[i-1][j]
                if left == -1:
                    left = 0
                if up == -1:
                    up = 0
                da[i][j] = left + up
            print_2d_arr(da)

    return da[n][m] % 1000000007

m, n = 4, 3
puddles = [[2, 2]]

answer = solution(n,m,puddles)
print(answer)