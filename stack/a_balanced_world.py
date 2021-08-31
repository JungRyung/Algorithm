'''
TITLE   : 균형잡힌 세상
URL     : https://www.acmicpc.net/problem/4949
DATE    : 21.08.31
'''
import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == '.':
        break
    s = []
    valid = True
    for char in sentence:
        if char == '(' or char == '[':
            s.append(char)
        elif char == ')':
            if len(s) > 0 and s[-1] == '(':
                s.pop()
            else:
                valid = False
                break
        elif char == ']':
            if len(s) > 0 and s[-1] == '[':
                s.pop()
            else:
                valid = False
                break
    if valid and len(s)==0:
        print("yes")
    else:
        print("no")
