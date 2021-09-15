'''
TITLE   : 명령 프롬프트
URL     : https://www.acmicpc.net/problem/2902
DATE    : 21.09.15
'''
import sys

n = int(sys.stdin.readline())

names = [sys.stdin.readline().strip() for _ in range(n)]

before = names[0]
len_name = len(names[0])
ans = list(before)
for name in names:
    for i in range(len_name):
        if before[i] != name[i]:
            ans[i] = '?'
print(''.join(ans))