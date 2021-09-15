'''
TITLE   : 소트인사이드
URL     : https://www.acmicpc.net/problem/1427
DATE    : 21.09.15
'''
import sys

nums = list(sys.stdin.readline().strip())
nums.sort(reverse=True)
print(''.join(nums))