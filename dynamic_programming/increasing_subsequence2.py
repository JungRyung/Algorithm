##### 증가하는 부분수열 #####
# URL : https://www.acmicpc.net/source/30560420
# 이분탐색으로 풀이
import bisect
n = int(input())
numbers = list(map(int, input().split()))
lis = []
for i in range(len(numbers)):
    if i == 0:
        lis.append(numbers[0])
    else:
        if lis[-1] >= numbers[i]:
            lis[bisect.bisect_left(lis,numbers[i])] = numbers[i]
        else:
            lis.append(numbers[i])
print(len(lis))