N, K = map(int, input().split())

arr_A = []
arr_B = []

arr_A = list(map(int,input().split()))
arr_B = list(map(int,input().split()))

for i in range(K):
    arr_A.sort()
    arr_B.sort()
    if arr_A[0] < arr_B[-1]:
        arr_A[0], arr_B[-1] = arr_B[-1], arr_A[0]
    else:
        break

sum = 0
for A in arr_A:
    sum += A

print(sum)
