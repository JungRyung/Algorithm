'''
TITLE   : 이항 계수 1
URL     : https://www.acmicpc.net/problem/11050
DATE    : 21.09.07
'''
from math import comb

n, k = map(int, input().split())
print(comb(n,k))