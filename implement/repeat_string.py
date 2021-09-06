'''
TITLE   : 문자열 반복
URL     : https://www.acmicpc.net/problem/2675
DATE    : 21.09.06
'''
import sys

for _ in range(int(sys.stdin.readline())):
    inputs = list(sys.stdin.readline().split())
    r, s = int(inputs[0]), inputs[1]
    for i in s:
        print(i*r,end='')
    print()