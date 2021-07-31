'''
TITLE   : 2 x n 타일링 2
URL     : https://www.acmicpc.net/problem/11727
DATE    : 21.07.31
'''
n = int(input())

dp = [0] * n

if n == 1:
    print(1)
else:
    dp[0] = 1
    dp[1] = 3
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]*2
    print(dp[n-1]%10007)