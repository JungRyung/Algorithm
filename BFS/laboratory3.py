'''
TITLE   : 연구소 3
URL     : https://www.acmicpc.net/problem/17142
DATE    : 21.08.17
'''
import sys
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
lab = [[] for _ in range(n)]
virus = []
q = deque()
for i in range(n):
    lab[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if lab[i][j] == 2:
            virus.append((i,j))
for comb in combinations(virus, 2):
    