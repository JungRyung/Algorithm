'''
TITLE   : 검증수
URL     : https://www.acmicpc.net/problem/2475
DATE    : 21.09.07
'''
nums = map(int, input().split())

sum = 0
for num in nums:
    sum += num*num
ans = sum %10
print(ans)