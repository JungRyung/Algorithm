'''
TITLE   : 에디터
URL     : https://www.acmicpc.net/problem/1406
DATE    : 21.10.31
'''
import sys

text = list(sys.stdin.readline().rstrip())
s_left = text[:]
s_right = []
for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L' and len(s_left) > 0:
        s_right.append(s_left.pop())
        continue
    if command[0] == 'D' and len(s_right) > 0:
        s_left.append(s_right.pop())
        continue
    if command[0] == 'B' and len(s_left) > 0:
        s_left.pop()
        continue
    if command[0] == 'P':
        s_left.append(command[1])
        continue

while s_right:
    s_left.append(s_right.pop())
print(''.join(s_left))