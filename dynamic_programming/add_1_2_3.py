##### 1, 2, 3 더하기 #####
# URL : https://www.acmicpc.net/problem/9095
t = int(input())
for _ in range(t):
    n = int(input())
    da = [0]*(n+1)
    da[0] = 1

    for i in range(1,n+1):
        if i-1 >= 0:
            da[i] += da[i-1]
        if i-2 >= 0:
            da[i] += da[i-2]
        if i-3 >= 0:
            da[i] += da[i-3]
    print(da[n])