'''
TITLE   : ACM 호텔
URL     : https://www.acmicpc.net/problem/10250
DATE    : 21.09.07
'''
import sys

for _ in range(int(sys.stdin.readline())):
    h, w, n = map(int, sys.stdin.readline().split())
    a = n % h
    b = n // h + 1
    if a == 0:
        a = h
        b -= 1
    a = str(a)
    if b < 10:
        b = '0' + str(b)
    else:
        b = str(b)
    print(a,b,sep='')