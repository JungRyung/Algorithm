'''
TITLE   : 연구소 3
URL     : https://www.acmicpc.net/problem/17142
DATE    : 21.08.17
'''
import sys

n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(lab)