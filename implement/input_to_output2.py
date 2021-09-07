'''
TITLE   : 그대로 출력하기 2
URL     : https://www.acmicpc.net/problem/11721
DATE    : 21.09.07
'''
import sys

txt_list = []
while True:
    tmp = sys.stdin.readline()
    if tmp:
        txt_list.append(tmp)
    else:
        break

for txt in txt_list:
    print(txt,end='')
print()