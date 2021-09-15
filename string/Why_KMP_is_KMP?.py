'''
TITLE   : KMP는 왜 KMP일까?
URL     : https://www.acmicpc.net/problem/2902
DATE    : 21.09.15
'''
import sys

names = sys.stdin.readline().split('-')

ans = ''
for name in names:
    ans += name[0]
print(ans)