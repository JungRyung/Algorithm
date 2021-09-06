'''
TITLE   : 다이얼
URL     : https://www.acmicpc.net/problem/5622
DATE    : 21.09.06
'''
import sys

word_to_num = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

words = list(sys.stdin.readline().strip())

sec = 0
for word in words:
    sec += word_to_num[ord(word)-65] + 1
print(sec)