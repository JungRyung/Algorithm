'''
TITLE   : 차집합
URL     : https://www.acmicpc.net/problem/1822
DATE    : 21.11.09
'''
import sys

na, nb = map(int, sys.stdin.readline().split())
setA = list(map(int, sys.stdin.readline().split()))
setB = list(map(int, sys.stdin.readline().split()))

setB_dict = {}
for num in setB:
    setB_dict[num] = True

ans = []
cnt = 0
for num in setA:
    if num not in setB_dict:
        cnt += 1
        ans.append(num)
ans.sort()

print(cnt)
if cnt > 0: 
    for i in range(cnt):
        print(ans[i], end=' ')
    print()
