'''
TITLE   : 문자열 폭발
URL     : https://www.acmicpc.net/problem/9935
DATE    : 21.09.14
'''
s1 = input().strip()
s2 = input().strip()
len_s2 = len(s2)

stack = []
for s in s1:
    stack.append(s)
    if stack[-1] == s2[-1] and ''.join(stack[-len_s2:]) == s2:
        del stack[-len_s2:]
answer = ''.join(stack)
if answer == '':
    print("FRULA")
else:
    print(answer)