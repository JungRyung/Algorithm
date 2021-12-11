'''
TITLE   : 분산처리
URL     : https://www.acmicpc.net/problem/1009
DATE    : 21.11.20
'''
import sys

rule = [1,5,6,0]
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10
    if a in rule:
        if a == 0:
            print(10)
        else:
            print(a)
    else:
        b = 4 + b%4
        a = str(a**b)
        print(a[-1])