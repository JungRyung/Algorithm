'''
TITLE   : 용액
URL     : https://www.acmicpc.net/problem/2467
DATE    : 21.07.30
'''
import sys

n = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

start = 0
end = n-1

res_start = solutions[0]
res_end = solutions[n-1]
res_sum = abs(res_start + res_end)

while start < end:
    sum = solutions[start] + solutions[end]
    if abs(sum) < res_sum:
        res_start = solutions[start]
        res_end = solutions[end]
        res_sum = abs(sum)
        if res_sum == 0:
            break
    if sum > 0:
        end -= 1
    elif sum < 0:
        start += 1

print("{} {}".format(res_start, res_end))