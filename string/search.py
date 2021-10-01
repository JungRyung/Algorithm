'''
TITLE   : 찾기
URL     : https://www.acmicpc.net/problem/1786
DATE    : 21.10.01
'''
import sys

def makeTable(pattern):
    patternSize = len(pattern)
    table = [0]*patternSize
    j = 0
    for i in range(1,patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table

t = sys.stdin.readline().replace('\n','')
p = sys.stdin.readline().replace('\n','')
n = len(t)
m = len(p)

# KMP 알고리즘
table = makeTable(p)

cnt = 0
ans = []
j = 0
for i in range(0,n):
    while j > 0 and t[i] != p[j]:
        j = table[j - 1]
    if t[i] == p[j]:
        if j == m - 1:
            cnt += 1
            ans.append(str(i - m + 2))
            j = table[j]
        else:
            j += 1

print(cnt)
print(' '.join(ans))