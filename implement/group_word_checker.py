'''
TITLE   : 그룹 단어 체커
URL     : https://www.acmicpc.net/problem/1316
DATE    : 21.09.07
'''
import sys

n = int(sys.stdin.readline())

ans = 0
for _ in range(n):
    word = sys.stdin.readline().strip()
    check = True
    before = ''
    visit = [False] * 26
    for ch in word:
        if ch != before and not visit[ord(ch)-97]:
            visit[ord(ch)-97] = True
        elif ch != before and visit[ord(ch)-97]:
            check = False
            break
        before = ch
    if check:
        ans += 1
print(ans)