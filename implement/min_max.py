'''
TITLE   : 최소, 최대
URL     : https://www.acmicpc.net/problem/10818
DATE    : 21.09.06
'''
import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
print(min(numbers),max(numbers))