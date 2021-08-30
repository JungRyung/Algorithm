'''
TITLE   : 요세푸스 문제
URL     : https://www.acmicpc.net/problem/1158
DATE    : 21.08.30
'''
import sys

n, k = map(int, sys.stdin.readline().split())

q = []
for i in range(1,n+1):
    q.append(i)

idx = 0
ans = []
while q:
    idx += k-1
    if idx >= len(q):
        idx %= len(q)
    ans.append(str(q.pop(idx)))

print('<',', '.join(ans),'>',sep='')