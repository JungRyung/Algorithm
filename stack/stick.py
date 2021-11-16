'''
TITLE   : 막대기
URL     : https://www.acmicpc.net/problem/17608
DATE    : 21.11.16
'''
import sys

n = int(sys.stdin.readline())
s = []

for _ in range(n):
    num = int(sys.stdin.readline())
    while s:
        if s[-1] > num:
            break
        else:
            s.pop()
    s.append(num)
print(len(s))