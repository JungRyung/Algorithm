'''
TITLE   : 합 구하기
URL     : https://www.acmicpc.net/problem/11441
DATE    : 21.09.12
'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sums = [0] * n
sum = 0
for num in enumerate(nums):
    idx, number = num
    sum += number
    sums[idx] = sum
sums = [0] + sums

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sums[b] - sums[a-1])
    