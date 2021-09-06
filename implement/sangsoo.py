'''
TITLE   : 상수
URL     : https://www.acmicpc.net/problem/2908
DATE    : 21.09.06
'''
import sys

a, b = sys.stdin.readline().split()
a = int(a[::-1])
b = int(b[::-1])
print(max(a,b))