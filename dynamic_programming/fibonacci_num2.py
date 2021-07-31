'''
TITLE   : 피보나치 수 2
URL     : https://www.acmicpc.net/problem/2748
DATE    : 21.07.31
'''
import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
else:
    dp = [0] * (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])