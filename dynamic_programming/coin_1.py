##### 동전 1 #####
# URL : https://www.acmicpc.net/problem/2293
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

da = [0] * (k+1)
da[0] = 1

for coin in coins:
    for i in range(coin,k+1):
        da[i] += da[i-coin]
print(da[k])