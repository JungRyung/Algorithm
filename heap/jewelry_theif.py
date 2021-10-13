'''
TITLE   : 보석 도둑
URL     : https://www.acmicpc.net/problem/1202
DATE    : 21.10.12
'''
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

jewelries = []
for _ in range(n):
    weight, price = map(int, sys.stdin.readline().split())
    heapq.heappush(jewelries, (weight, price))

weights = []
for _ in range(k):
    weights.append(int(sys.stdin.readline()))
weights.sort()

jewelry_prices = []
res = 0
for weight in weights:
    while len(jewelries) > 0 and weight >= jewelries[0][0]:
        curr = heapq.heappop(jewelries)[1]
        heapq.heappush(jewelry_prices, -curr)
    if jewelry_prices:
        res -= heapq.heappop(jewelry_prices)
print(res)