##### 가장 큰 증가 부분 수열 (Maximum Increasing Subsequence) #####
# URL : https://www.acmicpc.net/problem/11055
import sys
n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

da = [0]*n

for i in range(n):
    da[i] = seq[i]
    for j in range(i):
        if seq[j] < seq[i]:
            da[i] = max(da[i], da[j]+seq[i])
print(max(da))