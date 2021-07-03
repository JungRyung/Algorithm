##### 피보나치 수 5 #####
n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    d = [0]*(n+1)
    d[0] = 0
    d[1] = 1
    for i in range(2,n+1):
        d[i] = d[i-1] + d[i-2]
    print(d[n])