'''
TITLE   : 오큰수
URL     : https://www.acmicpc.net/problem/17298
DATE    : 21.10.09
'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

s = []
s.append(0)
ans = ['-1'] * n
for i in range(1,n):
    while s and nums[s[-1]] < nums[i]:
        ans[s.pop()] = str(nums[i])
    s.append(i)
print(' '.join(ans))