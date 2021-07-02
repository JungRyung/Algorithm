##### RGB 거리 #####
# URL : https://www.acmicpc.net/problem/1149
import sys

n = int(sys.stdin.readline())

costs = [[] for _ in range(n)]
for i in range(n):
    costs[i] = list(map(int, sys.stdin.readline().split()))

def find_min_cost(idx,color):
    if idx == n-1:
        return costs[idx][color]
    min_cost = 1001
    for i in range(3):
        if i != color:
            min_cost = min(min_cost, find_min_cost(idx+1,i))
    return costs[idx][color] + min_cost

answer = min(find_min_cost(0,0),find_min_cost(0,1),find_min_cost(0,2))

print(answer)