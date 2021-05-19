#### 모험자 길드 ####
N = int(input())

fear_rate = list(map(int, input().split()))

fear_rate.sort(reverse=True)
result = 0
cnt = 0
while fear_rate:
    num = fear_rate.pop()  
    cnt += 1
    if cnt >= num:
        result += 1
        cnt = 0

print(result)