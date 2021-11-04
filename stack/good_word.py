'''
TITLE   : 좋은 단어
URL     : https://www.acmicpc.net/problem/3986
DATE    : 21.11.04
'''
import sys

n = int(sys.stdin.readline())

cnt = 0
for _ in range(n):
    s = []
    words = list(sys.stdin.readline().rstrip())
    for word in words:
        if s and s[-1] == word:
            s.pop()
        else:
            s.append(word)
    if not s:
        cnt += 1
print(cnt)