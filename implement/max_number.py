'''
TITLE   : 최댓값
URL     : https://www.acmicpc.net/problem/2562
DATE    : 21.09.06
'''
import sys
max_num = 0
idx = 0
for i in range(1,10):
    number = int(sys.stdin.readline())
    if number > max_num:
        idx = i
        max_num = number
print(max_num)
print(idx)