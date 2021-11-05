'''
TITLE   : 비밀번호 찾기
URL     : https://www.acmicpc.net/problem/17219
DATE    : 21.11.05
'''
import sys

n, m = map(int, sys.stdin.readline().split())

passwords = {}
for _ in range(n):
    site, password = sys.stdin.readline().split()
    passwords[site] = password

for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(passwords[site])