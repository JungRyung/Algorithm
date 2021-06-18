##### 못생긴 수 #####
# 2,3,5 만을 소인수로 가지는 수
# n번째 못생긴 수 구하기
import math
n = int(input())
# dp = []
# l = math.ceil(math.log(2*n+1,3))
# print(l)
# def agly_num(num,level):
#     if level == l:
#         return
#     if num not in dp:
#         dp.append(num)
#         agly_num(num*2,level+1)
#         agly_num(num*3,level+1)
#         agly_num(num*5,level+1)
#     else:
#         return
# agly_num(1,0)
# dp.sort()
# print(dp)
# print(dp[n-1])

ugly = [0] * n
ugly[0] = 1
i2 = i3 = i5 = 0
next2, next3, next5 = 2,3,5

for l in range(1,n):
    ugly[l] = min(next2,next3,next5)
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])