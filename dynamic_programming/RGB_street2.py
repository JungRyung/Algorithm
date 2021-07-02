##### RGB 거리 #####
# URL : https://www.acmicpc.net/problem/1149
import sys

n = int(sys.stdin.readline())

costs = [[] for _ in range(n)]
for i in range(n):
    costs[i] = list(map(int, sys.stdin.readline().split()))

cost = [0]*3
for i in range(3):
    before = i
    cost[i] = costs[0][i]
    for j in range(1,n):
        min_cost = 1001
        for k in range(3):
            if before!= k:
                min_cost = min(min_cost,costs[j][k])
                tmp = k
        cost[i] += min_cost
        before = tmp
print(min(cost))