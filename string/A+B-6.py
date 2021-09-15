'''
TITLE   : A+B - 6
URL     : https://www.acmicpc.net/problem/10953
DATE    : 21.09.15
'''
import sys

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split(','))
    print(a+b)