'''
TITLE   : 제로
URL     : https://www.acmicpc.net/problem/10773
DATE    : 21.08.31
'''
import sys

s = []
k = int(sys.stdin.readline())
for _ in range(k):
    num = int(sys.stdin.readline())
    if num > 0:
        s.append(num)
    else:
        s.pop()
print(sum(s))