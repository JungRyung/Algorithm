'''
TITLE   : 알파벳 찾기
URL     : https://www.acmicpc.net/problem/10809
DATE    : 21.09.06
'''
import sys
s = sys.stdin.readline().strip()
ans = []
for i in range(97,123):
    ans.append(str(s.find(chr(i))))
print(' '.join(ans))