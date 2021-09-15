'''
TITLE   : 직각삼각형
URL     : https://www.acmicpc.net/problem/4153
DATE    : 21.09.14
'''
import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==0 and b==0 and c==0:
        break
    sides = [a,b,c]
    max_side = max(sides)
    sides.remove(max_side)
    if max_side**2 == sides[0]**2 + sides[1]**2:
        print("right")
    else:
        print("wrong")