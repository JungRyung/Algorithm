N = int(input())

K = list(map(int,input().split()))

a = [0] * N
# a[:2] = K[:2]

a[0] = K[0]
a[1] = max(K[0], K[1])

for i in range(2,N):
    a[i] = max(a[i-1], a[i-2] + K[i])

print(a[N-1])
