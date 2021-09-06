'''
TITLE   : OX퀴즈
URL     : https://www.acmicpc.net/problem/8958
DATE    : 21.09.06
'''
import sys

for _ in range(int(sys.stdin.readline())):
    results = list(sys.stdin.readline().strip())
    cnt = 0
    score = 0
    for result in results:
        if result == 'O':
            cnt += 1
        else:
            cnt = 0
        score += cnt
    print(score)