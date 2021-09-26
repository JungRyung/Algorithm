'''
TITLE   : 접미사 배열
URL     : https://www.acmicpc.net/problem/10610
DATE    : 21.09.26
'''
import sys

s = list(sys.stdin.readline().strip())

suffixes = []
for i in range(len(s)):
    suffixes.append(''.join(s[i:]))
suffixes.sort()

print('\n'.join(suffixes))