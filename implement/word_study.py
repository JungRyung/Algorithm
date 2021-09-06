'''
TITLE   : 단어 공부
URL     : https://www.acmicpc.net/problem/1157
DATE    : 21.09.06
'''
import sys
word = sys.stdin.readline().strip()
ans = []
for i in range(65,91):
    upper = chr(i)
    lower = chr(i+32)
    ans.append((word.count(upper) + word.count(lower), upper))
max_num = 0
alphabet = ''
cnt = 0
for an in ans:
    num, alpha = an
    if num > max_num:
        max_num = num
        alphabet = alpha
        cnt = 1
    elif num == max_num:
        cnt += 1
if cnt > 1:
    print('?')
else:
    print(alphabet)