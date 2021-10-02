'''
TITLE   : 쇠막대기
URL     : https://www.acmicpc.net/problem/10799
DATE    : 21.10.01
'''
import sys

stick = sys.stdin.readline().strip()

stack = []
before = ''
ans = 0
for ch in stick:
    if ch == '(':
        stack.append(ch)
    else:
        # 레이저인 경우
        if before == '(':
            stack.pop()
            ans += len(stack)
        # 레이저가 아닌경우 -> 한 막대의 끝
        else:
            stack.pop()
            ans += 1
    before = ch

print(ans)