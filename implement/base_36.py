'''
TITLE   : 36진수
URL     : https://www.acmicpc.net/problem/1036
DATE    : 21.08.16
'''
import sys

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(sys.stdin.readline().strip())
print(numbers)
k = int(sys.stdin.readline())