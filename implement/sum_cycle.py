'''
TITLE   : 더하기 사이클
URL     : https://www.acmicpc.net/problem/1110
DATE    : 21.09.06
'''
n = int(input())
if n<10:
    left = 0
    right = n
else:
    left = n // 10
    right = n % 10
next = right * 10 + (left + right) % 10
cnt = 1
while next != n:
    if next<10:
        left = 0
        right = next
    else:
        left = next // 10
        right = next % 10
    next = right * 10 + (left + right) % 10
    cnt += 1
print(cnt)