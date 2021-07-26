'''
TITLE   : 게임 개발
URL     : https://www.acmicpc.net/problem/1516
DATE    : 21.07.26
'''
import sys

n = int(sys.stdin.readline())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
for _ in range(n):
    