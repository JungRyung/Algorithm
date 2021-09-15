'''
TITLE   : 알파벳 개수
URL     : https://www.acmicpc.net/problem/1541
DATE    : 21.09.15
'''
import sys

sum_ap = [0] * (ord('z')-ord('a')+1)

word = sys.stdin.readline().strip()

for ch in word:
    sum_ap[ord(ch)-ord('a')] += 1
for ans in sum_ap:
    print(ans,end=' ')
print()