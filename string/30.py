'''
TITLE   : 30
URL     : https://www.acmicpc.net/problem/10610
DATE    : 21.09.24
'''
import sys
from itertools import permutations
import heapq

nums = list(sys.stdin.readline().strip())
nums.sort(reverse=True)
answer = -1

if min(nums) == '0':
    num = int(''.join(nums))
    if num % 3 == 0:
        answer = num

print(answer)