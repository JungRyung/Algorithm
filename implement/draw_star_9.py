##### 별 찍기 - 9 #####
# URL : https://www.acmicpc.net/problem/2446
n = int(input())
m = n
while m>0:
    i = 2*m-1
    j = n-m
    for k in range(j):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()
    m -= 1

m = 2
while m<=n:
    i = 2*m-1
    j = n-m
    for k in range(j):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    print()
    m += 1