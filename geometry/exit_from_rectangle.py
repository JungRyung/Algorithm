'''
TITLE   : 직사각형에서 탈출
URL     : https://www.acmicpc.net/problem/1085
DATE    : 21.09.14
'''
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))