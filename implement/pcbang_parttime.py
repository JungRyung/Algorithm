'''
TITLE   : 피시방 알바
URL     : https://www.acmicpc.net/problem/1453
DATE    : 21.08.15
'''
import sys

n = int(sys.stdin.readline())
customers = list(map(int, sys.stdin.readline().split()))
customers_set = set(customers)

print(len(customers) - len(customers_set))