'''
TITLE   : 수 정렬하기
URL     : https://www.acmicpc.net/problem/2750
DATE    : 21.09.06
'''
import sys
n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
numbers.sort()
for number in numbers:
    print(number)