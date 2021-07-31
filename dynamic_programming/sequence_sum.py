'''
TITLE   : 연속 합
URL     : https://www.acmicpc.net/problem/1912
DATE    : 21.07.31
'''
import sys
import copy
LOWEST = -1001

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = copy.deepcopy(numbers)

max_sum = LOWEST
q = []
for i in range(n):
    if i > 0 and dp[i-1] > 0:
        dp[i] = dp[i-1] + numbers[i]
    max_sum = max(max_sum, dp[i])
print(max_sum)
    
        