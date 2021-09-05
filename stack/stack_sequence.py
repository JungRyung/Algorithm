'''
TITLE   : 스택 수열
URL     : https://www.acmicpc.net/problem/1874
DATE    : 21.08.31
'''
import sys

s = []
command = []
n = int(sys.stdin.readline())
number = 1
flag = True
for _ in range(n):
    num = int(sys.stdin.readline())
    # 스택이 비어있거나 top이 수열의 현재 요소보다 작은 경우 push
    while len(s)==0 or s[-1] < num:
        if number <= n:
            s.append(number)
            number += 1
            command.append('+')
        else:
            flag = False
            break
    if len(s)>0 and s[-1] == num:
        s.pop()
        command.append('-')
    else:
        flag = False
        break
if flag:
    print('\n'.join(command))
else:
    print('NO')
    