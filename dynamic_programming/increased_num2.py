n = int(input())
da = [[0] * 10 for _ in range(n + 1)]
da[1] = [1] * 10
for i in range(2, n + 1):
    da[i][0] = 1
    for j in range(10):
        da[i][j] = da[i - 1][j] + da[i][j - 1]
print(sum(da[n]) % 10007)