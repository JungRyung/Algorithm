'''
TITLE   : 두 수 비교하기
URL     : https://www.acmicpc.net/problem/1330
DATE    : 21.09.06
'''
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')