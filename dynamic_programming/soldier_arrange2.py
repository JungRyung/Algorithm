##### 병사 배치하기 ######
# LIS(Longest Increasing Subsequence) -> 반복문으로 구현(DP 포함)
import sys

n = int(sys.stdin.readline())
soldiers = list(map(int,sys.stdin.readline().split()))
dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if soldiers[i] < soldiers[j]:
            dp[i] = max(dp[i], dp[j]+1)

lds_num = max(dp)
answer = n - lds_num
print(answer)