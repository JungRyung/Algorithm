##### 01타일 #####
# URL : https://www.acmicpc.net/problem/1904
n = int(input())

da = [0] * (n+1)
da[0] = 1
da[1] = 1

if n == 1:
    print(1)
else:
    for i in range(2,n+1):
        da[i] = (da[i-1] + da[i-2])%15746
        print(da[i])
    print(da[n])
