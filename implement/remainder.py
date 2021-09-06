'''
TITLE   : 나머지
URL     : https://www.acmicpc.net/problem/10430
DATE    : 21.09.06
'''
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c) + (b%c)) % c)
print((a*b)%c)
print(((a%c) * (b%c)) % c)