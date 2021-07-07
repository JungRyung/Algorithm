##### 오르막 수 #####
# URL : https://www.acmicpc.net/problem/11057

n = int(input())
da = [[1]*10 if i==0 else [0]*10 for i in range(n)]
if n==1:
    print(10)
else:
    for i in range(1,n):
        for j in range(10):
            for k in range(j,10):
                da[i][j] += da[i-1][k]
    print(sum(da[n-1])%10007)