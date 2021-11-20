'''
TITLE   : 분산처리
URL     : https://www.acmicpc.net/problem/1009
DATE    : 21.11.20
'''
import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    c = a
    for __ in range(b-1):
        c = c * a % 10
    print(c)

