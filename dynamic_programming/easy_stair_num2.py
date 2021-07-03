##### 쉬운 계단 수 #####
# URL : https://www.acmicpc.net/problem/10844
n = int(input())

d = [[0] * 10 for _ in range(n)]
if n == 1:
    print(9)
else:
    for i in range(1,10):
        d[0][i] = 1
    for i in range(1,n):
        for j in range(10):
            if j == 0: 
                d[i][j] = d[i-1][j+1]
            elif j == 9:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]
    cnt = 0
    for i in range(10):
        cnt += d[n-1][i]
    print(cnt%1000000000)
