##### 편집 거리 #####
str_A = input()
str_B = input()
dp = [[0]*(len(str_B)+1) for _ in range(len(str_A)+1)]
cnt = 0
for i in range(len(str_B)+1):
    dp[0][i] = cnt
    cnt += 1
cnt = 0
for i in range(len(str_A)+1):
    dp[i][0] = cnt
    cnt += 1

for i in range(1, len(str_A)+1):
    for j in range(1, len(str_B)+1):
        if str_A[i-1] == str_B[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

print(dp)
print(dp[-1][-1])