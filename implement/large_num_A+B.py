'''
TITLE   : 큰 수 A+B
URL     : https://www.acmicpc.net/problem/10757
DATE    : 21.09.07
'''
import sys

a, b = sys.stdin.readline().split()
a = a[::-1]
b = b[::-1]
len_a = len(a)
len_b = len(b)
list_a = [0]*6
list_b = [0]*6

idx = 0
k = 0
for i in range(len_a//10):
    tmp = a[i*10:i*10+10]
    list_a[i] = int(tmp[::-1])
    idx += 10
    k += 1
if len_a % 10 != 0:
    tmp = a[idx:]
    list_a[k] = int(tmp[::-1])

idx = 0
k = 0
for i in range(len_b//10):
    tmp = b[i*10:i*10+10]
    list_b[i] = int(tmp[::-1])
    idx += 10
    k += 1
if len_b % 10 != 0:
    tmp = b[idx:]
    list_b[k] = int(tmp[::-1])

round = 0
ans = []
for i in range(6):
    sum = list_a[i] + list_b[i] + round
    if sum >= 10000000000:
        ans.append(sum % 10000000000)
        round = 1
    else:
        ans.append(sum)
        round = 0

for i in ans[::-1]:
    if i > 0:
        print(i,end='')
print()
