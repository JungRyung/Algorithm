'''
TITLE   : 카드
URL     : https://www.acmicpc.net/problem/11652
DATE    : 21.11.02
'''
import sys

n = int(sys.stdin.readline())
cards = {}
for _ in range(n):
    num = int(sys.stdin.readline())
    if num not in cards:
        cards[num] = 1
    else:
        cards[num] += 1

tuples = []
for card in cards:
    tuples.append((-cards[card], card))
tuples.sort()
print(tuples[0][1])