##### 가장 긴 증가 부분 수열 2 #####
# URL : https://www.acmicpc.net/problem/12015
import sys
import bisect

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

lis = []
lis.append(seq[0])

for num in seq:
    if num > lis[-1]:
        lis.append(num)
    elif num < lis[-1]:
        lis[bisect.bisect_left(lis,num)] = num
print(len(lis))