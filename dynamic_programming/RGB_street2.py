##### RGB 거리 #####
# URL : https://www.acmicpc.net/problem/1149
import sys

n = int(sys.stdin.readline())

costs = [[] for _ in range(n)]
for i in range(n):
    costs[i] = list(map(int, sys.stdin.readline().split()))

da = [[0]*3 for _ in range(n)]
da[0] = costs[0]
for i in range(1,n):
    da[i][0] = min(da[i-1][1], da[i-1][2]) + costs[i][0]
    da[i][1] = min(da[i-1][0], da[i-1][2]) + costs[i][1]
    da[i][2] = min(da[i-1][0], da[i-1][1]) + costs[i][2]
print(min(da[n-1]))