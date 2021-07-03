##### 증가하는 부분수열 #####
# URL : https://www.acmicpc.net/source/30560420
n = int(input())
numbers = list(map(int, input().split()))

d = [0] * (1001)
for number in numbers:
    if d[number] == d[number-1]:
        for i in range(number,1001):
            if d[i] == d[number-1]+1:
                break
            d[i] = d[number-1]+1
print(d[-1])