import sys
import heapq
n = int(sys.stdin.readline())
cards = []
for i in range(n):
    heapq.heappush(cards,int(sys.stdin.readline()))
answer = 0
while len(cards)>1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    sum = card1 + card2
    answer += sum
    heapq.heappush(cards,sum)
print(answer)