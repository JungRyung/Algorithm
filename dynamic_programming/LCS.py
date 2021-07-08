##### LCS(Longest Common Subsequence) #####
# URL : https://www.acmicpc.net/problem/9251
import sys
str1 = [0] + list(sys.stdin.readline().strip())
str2 = [0] + list(sys.stdin.readline().strip())
len_str1 = len(str1)
len_str2 = len(str2)
da = [[0]*len_str2 for _ in range(len_str1)]
for i in range(1,len_str1):
    for j in range(1,len_str2):
        if str1[i] == str2[j]:
            da[i][j] = da[i-1][j-1] + 1
        else:
            da[i][j] = max(da[i-1][j], da[i][j-1])
print(da[len_str1-1][len_str2-1])