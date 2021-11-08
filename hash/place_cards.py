'''
TITLE   : 카드 놓기
URL     : https://www.acmicpc.net/problem/5568
DATE    : 21.11.08
'''
import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

cards = []
for _ in range(n):
    cards.append(sys.stdin.readline().rstrip())
    
cards_comb = list(permutations(cards,k))
ans = {}
for i in range(len(cards_comb)):
    ans[''.join(cards_comb[i])] = True
print(len(ans))