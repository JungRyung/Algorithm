'''
TITLE   : 잃어버린 괄호
URL     : https://www.acmicpc.net/problem/1541
DATE    : 21.09.15
'''
import sys

expression = list(sys.stdin.readline().strip())

num = ''
minus = False
front = [0]
behind = [0]
for char in expression:
    if ord('0')<=ord(char)<=ord('9'):
        num += char
    else:
        if not minus:
            front.append(int(num))
            num = ''
        else:
            behind.append(int(num))
            num = ''
        if char == '-':
            minus = True
if not minus:
    front.append(int(num))
else:
    behind.append(int(num))

print(sum(front) - sum(behind))