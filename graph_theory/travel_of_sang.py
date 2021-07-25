'''
Title   : 여행 가자
URL     : https://www.acmicpc.net/problem/1976
DATE    : 21.07.25
'''
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges.append((a,b))
    print(n-1)