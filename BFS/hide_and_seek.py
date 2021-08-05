'''
TITLE   : 숨바꼭질
URL     : https://www.acmicpc.net/problem/1697
DATE    : 21.08.06
'''
import sys

n, k = map(int, sys.stdin.readline().split())

visit = [False]*100001

visit[n] = True
q = []
q.append((n,0))
while q:
    curr, t = q.pop(0)
    if curr == k:
        print(t)
        break
    for next in [curr-1, curr+1, curr*2]:
        if 0<=next<=100000 and not visit[next]:
            visit[next] = True
            q.append((next, t+1))