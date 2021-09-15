'''
TITLE   : 듣보잡
URL     : https://www.acmicpc.net/problem/1764
DATE    : 21.09.15
'''
import sys

n, m = map(int, sys.stdin.readline().split())
not_heard = set()
not_seen = set()
for _ in range(n):
    not_heard.add(sys.stdin.readline().strip())
for _ in range(m):
    not_seen.add(sys.stdin.readline().strip())
answers = list(not_heard & not_seen)
answers.sort()
print(len(answers))
print('\n'.join(answers))