'''
TITLE   : 숫자 카드 2
URL     : https://www.acmicpc.net/problem/10816
DATE    : 21.10.01
'''
import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums_dic = {}
for num in nums:
    if num in nums_dic:
        nums_dic[num] += 1
    else:
        nums_dic[num] = 1

m = int(sys.stdin.readline())
search_nums = list(map(int, sys.stdin.readline().split()))

ans = []
for num in search_nums:
    if num in nums_dic:
        ans.append(str(nums_dic[num]))
    else:
        ans.append('0')

print(' '.join(ans))