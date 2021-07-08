##### 동전 2 #####
# URL : https://www.acmicpc.net/problem/2294
import sys
INF = 1e9
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
coins.sort()
da = [INF] * (k+1)
da[0] = 0

for i in range(1,k+1):
    for coin in coins:
        if i < coin:
            break
        da[i] = min(da[i], da[i-coin] + 1)
print(da[k] if da[k] != INF else -1)