'''
TITLE   : 열 개씩 끊어 출력하기
URL     : https://www.acmicpc.net/problem/11721
DATE    : 21.09.07
'''
import sys

word = sys.stdin.readline().strip()
length = len(word)
a = length // 10
ans = []

idx = 0
for i in range(a):
    ans.append(word[i*10:i*10+10])
    idx += 10
ans.append(word[idx:])

print('\n'.join(ans))