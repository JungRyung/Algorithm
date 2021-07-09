##### 가장 긴 감소하는 부분수열 #####
# URL : https://www.acmicpc.net/problem/11722
import sys
import bisect

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

lds = []
lds.append(seq[-1])
for num in seq[::-1]:
    if num < lds[-1]:
        lds[bisect.bisect_left(lds,num)] = num
    elif num > lds[-1]:
        lds.append(num)
print(len(lds))