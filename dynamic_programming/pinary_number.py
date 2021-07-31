'''
TITLE   : 이친수
URL     : https://www.acmicpc.net/problem/2193
DATE    : 21.07.31
'''
n = int(input())
dp = [[0]*2 for _ in range(n)]

dp[0][0] = 0
dp[0][1] = 1
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(dp[n-1][0] + dp[n-1][1])