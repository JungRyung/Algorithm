##### 팰린드롬? #####
# URL : https://www.acmicpc.net/problem/10942
import sys

def print_2D_arr(arr):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end='\t')
        print()

n = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
da = [[False]*(n+1) for _ in range(n+1)]

m = int(sys.stdin.readline())

for i in range(1,n+1):
    da[i][i] = True
    if num[i] == num[i-1]:
        da[i-1][i] = True

for i in range(2,n):
    for j in range(1,n-i+1):
        if num[j] == num[j+i] and da[j+1][j+i-1]:
            da[j][j+i] = True
print_2D_arr(da)

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    if da[s][e]:
        print(1)
    else:
        print(0)