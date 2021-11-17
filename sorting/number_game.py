'''
TITLE   : 숫자놀이
URL     : https://www.acmicpc.net/problem/1755
DATE    : 21.11.17
'''
import sys

m, n = map(int, sys.stdin.readline().split())

num_tuple = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
num_list = []
def num_to_string(num):
    first = num // 10
    second = num % 10
    if num > 9:
        return num_tuple[first] + ' ' + num_tuple[second]
    else:
        return num_tuple[second]

for i in range(m,n+1):
    num_list.append((num_to_string(i), i))
    
num_list.sort()

cnt = 0
for i in range(len(num_list)):
    cnt += 1
    print(num_list[i][1],end='')
    if cnt == 10:
        cnt = 0
        print()
    else:
        print(' ',end='')