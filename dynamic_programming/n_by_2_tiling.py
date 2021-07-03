##### nX2 타일링 #####
# URL : https://www.acmicpc.net/problem/11726
n = int(input())

d = [0]*n
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    d[0] = 1
    d[1] = 2
    for i in range(2,n):
        d[i] = d[i-1] + d[i-2]

    print(d[n-1]%10007)