'''
TITLE   : 괄호
URL     : https://www.acmicpc.net/problem/9012
DATE    : 21.08.30
'''
import sys

n = int(sys.stdin.readline())
for _ in range(n):
    brackets = list(sys.stdin.readline().strip())
    num = 0
    for bracket in brackets:
        if bracket == '(':
            num += 1
        else:
            if num > 0:
                num -= 1
            else:
                num = -1
                break
    if num == 0:
        print("YES")
    else:
        print("NO")