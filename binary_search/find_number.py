'''
TITLE   : 수 찾기
URL     : https://www.acmicpc.net/problem/1920
DATE    : 21.07.28
'''
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

m = int(sys.stdin.readline())
search_nums = list(map(int, sys.stdin.readline().split()))

def bisect(left, right, num):
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] > num:
            right = mid - 1
        elif numbers[mid] < num:
            left = mid + 1
        else:
            return True
    return False
        

for num in search_nums:
    searched = bisect(0, n-1, num)
    if searched:
        print(1)
    else:
        print(0)