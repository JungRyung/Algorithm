'''
TITLE   : X보다 작은 수
URL     : https://www.acmicpc.net/problem/10871
DATE    : 21.09.06
'''
import sys

n, x = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

ans = []
for number in numbers:
    if number < x:
        ans.append(str(number))
print(' '.join(ans))