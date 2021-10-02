'''
TITLE   : 카드2
URL     : https://www.acmicpc.net/problem/2164
DATE    : 21.10.01
'''
import sys
from collections import deque

n = int(sys.stdin.readline())
cards = [i+1 for i in range(n)]
cards = deque(cards)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards.pop())