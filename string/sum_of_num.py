'''
TITLE   : 숫자의 합
URL     : https://www.acmicpc.net/problem/11720
DATE    : 21.09.15
'''
import sys

n = int(sys.stdin.readline())
nums = list(sys.stdin.readline().strip())
sum = 0
for num in nums:
    sum += int(num)
print(sum)