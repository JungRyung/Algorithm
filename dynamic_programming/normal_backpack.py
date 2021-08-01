'''
TITLE   : 평범한 배낭
URL     : https://www.acmicpc.net/problem/12865
DATE    : 21.08.01
'''
import sys

n, k = map(int, sys.stdin.readline().split())
weights = [0] * (n+1)
values = [0] * (n+1)
for i in range(1, n+1):
    w, v = map(int, sys.stdin.readline().split())
    weights[i] = w
    values[i] = v

dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j-weights[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]]+ values[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])